import json
from pprint import pprint
from collections import defaultdict

with open('data_edited.json') as data_file:    
    data = json.load(data_file)
    dic={}
    dic = defaultdict(lambda: 0, dic)
    lis=[]
    dic_list={}
    dic_list=defaultdict(lambda: 0, dic_list)
    for d in data:
        for key,val in d.items():
            dic_list[key]+=1
    for d in data:
        for key,value in d.items():
            #print (key)
            for val in d[key]:
                dic[key]+=(d[key][val])
    for key in dic:
        print(key, dic[key]/dic_list[key])
