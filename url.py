
import os
import time
import pyshark
import json
from collections import defaultdict
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
    return length
    
dic={}
url_list = ['https://stackoverflow.com/questions/23569441/is-it-possible-to-apply-css-to-half-of-a-character']
fh = open("test1.pcap",'r')
fh.close()
os.system('sudo chmod 777 test1.pcap')
for i in url_list:
    os.system('wget' + ' ' +i)
    time.sleep(10)
    dic[i] = Analysis(i)
    
    
with open('data.json', 'a') as outfile:
    json.dump(dic, outfile)
