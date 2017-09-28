
import os
import time
import pyshark
import json
def Analysis(url):
    cap = pyshark.FileCapture('test1.pcap')
    dic = {}
    length = {}
    packet1 = cap[0]
    IP = packet1['ip']
    length['len'] = IP._all_fields['ip.len']
    return length
    
    
url_list = ['https://www.stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output','https://www.stackoverflow.com/questions/17824096/bufsize-must-be-an-integer-error-while-grepping-a-message','https://www.stackoverflow.com/questions/3797958/how-to-write-script-output-to-file-and-command-line']
dic = {}
for i in url_list:
    os.system('wget' + ' ' +i)
    time.sleep(10)
    dic[i] = Analysis(i)
    os.system('echo > test1.pcap')
    
with open('data.txt', 'w') as outfile:
    json.dump(dic, outfile)
