from ipaddress import *
from itertools import product as pd
net = ip_network('49.26.38.163/255.255.255.224', 0)
print(net.num_addresses)
k = 0
for x in pd('01', repeat=5):
    s = ''.join(x)
    if s not in ('11111', '00000'):
        if int(s, 2) % 2 == 0:
            k += 1
print(k)
# 15
