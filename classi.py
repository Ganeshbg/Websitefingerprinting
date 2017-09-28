import os
import subprocess
x = subprocess.call(['sudo','tcpdump', '-vv', 'host stackoverflow.com','-w','test1.pcap'])