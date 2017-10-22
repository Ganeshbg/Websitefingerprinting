import json
from pprint import pprint
from collections import defaultdict

sum_dict = {}
omit_lengths = [64, 60,52,254,1500,310,40,83,178,626]
with open('new_url_data.json') as data_file:
    data=json.load(data_file)
    dic_list= {}
    for d in data:
	urls = d.keys()
	url = urls[0]
	list_of_lengths = d[url].keys() 
	size = 0
	for len in list_of_lengths:
		if(int(len) not in omit_lengths):
		    size = size + (int(len) * d[url][len])
	print(size)
	sum_dict[url] = size
i=1	
for elem in sum_dict:
	print( i, str(elem) , sum_dict[elem])
	
	
