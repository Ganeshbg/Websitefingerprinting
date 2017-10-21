import json
from pprint import pprint

sum_dict = {}
omit_lengths = [64, 60,52,254,1500,310,40,83,178,626]
with open('data.json') as data_file:
    data=json.load(data_file)
    for d in data:
	urls = d.keys()
	url = urls[0]
	list_of_lengths = d[url].keys() 
	size = 0
	for len in list_of_lengths:
		
		if(int(len) not in omit_lengths):
		    size = size + (int(len) * d[url][len])
	#print(size)
	if url in sum_dict:
		sum_dict[url] += size
	else:
		sum_dict[url] = size 
i = 1
for elem in sum_dict:
	sum_dict[elem] = sum_dict[elem]/3
	print( i, sum_dict[elem])
	i = i+1	
	
