from ipaddress import *


for mask in range(33):
    net = ip_network(f'145.192.94.230/{mask}', 0)
    print(net, net.netmask)
# 145.192.80.0/20 255.255.240.0
# 240
