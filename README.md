# Websitefingerprinting

A classifier which helps recognise the URL accessed by a user on https traffic.

In HTTPS traffic, the packets with host and URL details are encrypted. We cannot use or look into the headers to get the details 
of host and the URL. However, few details of a request are fingerprintable. We are concentrating only on the host "stackoverflow".
Our code captures packets only for the requests that are made for "www.stackoverflow.com". We use Pyshark to parse through every 
packet and get the length of each packet. We then create a dictionary of key value pairs where key = length of packet, value = frequency
of length of packet. This dictionary is a value for another dictionary whose keys are the URL.

Example: {'www.stackoverflow.com/a/b':{'65':120,'76:78,'34':332}}
