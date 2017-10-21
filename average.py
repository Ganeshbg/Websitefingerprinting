import json
from pprint import pprint

sum_dict = {}
omit_lengths = [64, 60,52,254,1500,310,40,83,178,626]
with open('data.json') as data_file:
    data=json.load(data_file)
    for d in data:
	#print(d.keys())
	urls = d.keys()
	#print type(urls)
	#print (urls[0])
	#print(d[urls[0]].keys())
	list_of_lengths = d[urls[0]].keys() 
	size = 0
	for len in list_of_lengths:
		#print (d[urls[0]][len])
		if(int(len) not in omit_lengths):
		    size = size + (int(len) * d[urls[0]][len])
	#print(size)
	if urls[0] in sum_dict:
		sum_dict[urls[0]] += size
	else:
		sum_dict[urls[0]] = size 
i = 1
for elem in sum_dict:
	sum_dict[elem] = sum_dict[elem]/3
	print( i, sum_dict[elem])
	i = i+1	
	
