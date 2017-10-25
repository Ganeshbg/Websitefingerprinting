import json
from pprint import pprint
from collections import defaultdict
import os
import time
import pyshark
sum_dict = {}
omit_lengths = [64,60,52,310,40,83,178]

def Analysis(url):
    cap = pyshark.FileCapture('test1.pcap')
    #dic = {}
    length = {}
    length=defaultdict(lambda:1,length)
    print (len(cap))
    for i in cap:
        #print (i['ip']._all_fields['ip.len'])
        packet = i
        IP = packet['ip']
        x = IP._all_fields['ip.len']
        length[x] += 1
        #print(length[x])
    os.system('echo ''> test1.pcap')
    #print (length)
    sum1=0
    packets=0
    mid_size=0
    mid_packets=0
    for i in length:
        sum1=sum1+(int(i)*int(length[i]))
        packets=packets+(int(length[i]))
        if(int(i) not in omit_lengths):
            mid_size+=int(i)*length[i]
            mid_packets+=length[i]
    #print ("length per packet:",sum1/packets,"Number of packets:", packets,"length per mid packet:", mid_size/mid_packets)
    #print (length)
    return(sum1/packets,packets,mid_size/mid_packets)


url_list = ['https://stackoverflow.com/questions/46845387/how-to-hide-table-footer-in-table-component-using-something-alike-printwhenexpr']
fh = open("test1.pcap",'r')
fh.close()
os.system('sudo chmod 777 test1.pcap')
for i in url_list:
    os.system('wget' + ' ' +i)
    time.sleep(5)
    length_per_pac, pac_len, length_per_mid_pac=Analysis(i)
with open('data_final.json') as data_file:
    data=json.load(data_file)
    url=[]
    avg_pckt_len={}
    avg_pckt_len=defaultdict(lambda: [0,0], avg_pckt_len)
    pac_count={}
    pac_count=defaultdict(lambda: [0,0], pac_count)
    mid_pckt_len={}
    mid_pckt_len=defaultdict(lambda: [0,0], mid_pckt_len)
    for d in data:
        urls = list(d.keys())
        url = urls[0]
        list_of_lengths = d[url].keys() 
        size = 0
        num_pac=0
        mid_size=0
        mid_packets=0
        for len in list_of_lengths:	
            size = size + (int(len) * d[url][len])
            num_pac+=d[url][len]
            if(int(len) not in omit_lengths):
                mid_size = mid_size + (int(len) * d[url][len])
                mid_packets+=d[url][len]
        size=size/num_pac
        mid_size=mid_size/mid_packets
        if(avg_pckt_len[url][0]==0 ):
            avg_pckt_len[url][0]=size
        elif(size<avg_pckt_len[url][0]):
            avg_pckt_len[url][0]=size
        elif (size>avg_pckt_len[url][1]):
            avg_pckt_len[url][1]=size
        if (pac_count[url][0]==0):
            pac_count[url][0]=num_pac
        elif(num_pac<pac_count[url][0]):
            pac_count[url][0]=num_pac
        elif(num_pac>pac_count[url][1]):
            pac_count[url][1]=num_pac
        if(mid_pckt_len[url][0]==0 ):
            mid_pckt_len[url][0]=mid_size
        elif(mid_size<mid_pckt_len[url][0]):
            mid_pckt_len[url][0]=mid_size
        elif (mid_size>mid_pckt_len[url][1]):
            mid_pckt_len[url][1]=mid_size
    final_list=[]
    for i in avg_pckt_len:
        if((length_per_pac>avg_pckt_len[i][0]) & (length_per_pac<avg_pckt_len[i][1])):
            if((pac_len>pac_count[i][0]) & (pac_len<pac_count[i][1])):
                if((length_per_mid_pac>mid_pckt_len[i][0]) & (length_per_mid_pac<mid_pckt_len[i][1])):
                    final_list.append(i)
           
    #print (len(final_list))
    print (final_list.__len__())
    print (final_list)
    print (length_per_pac, pac_len, length_per_mid_pac)
    print (url_list[0])
    if(url_list[0] in final_list):
        print ("Yes URL found")
        
        
