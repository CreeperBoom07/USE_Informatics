from ipaddress import *

net = ip_network('0.0.0.0/255.255.240.0')
print(net.num_addresses - 2)
# 4094
