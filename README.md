# Websitefingerprinting

A classifier which helps recognise the URL accessed by a user on https traffic.

In HTTPS traffic, the packets with host and URL details are encrypted. We cannot use or look into the headers to get the details 
of host and the URL. However, few details of a request are fingerprintable. We are concentrating only on the host "stackoverflow".
Our code captures packets only for the requests that are made for "www.stackoverflow.com". We use Pyshark to parse through every 
packet and get the length of each packet. We then create a dictionary of key value pairs where key = length of packet, value = frequency
of length of packet. This dictionary is a value for another dictionary whose keys are the URL.

Example: {'www.stackoverflow.com/a/b':{'65':120,'76:78,'34':332}}

When a new request is made we compare the frequency of packet lengths for that request and try to map it with the frequencies that we have already saved.

This implementation is based out of the paper http://www.cs.jhu.edu/~sdoshi/jhuisi650/papers/spimacs/SPIMACS_CD/ccsw/p31.pdf
Take a look at the "sub" branch for current updates code. The project is still in progress.
