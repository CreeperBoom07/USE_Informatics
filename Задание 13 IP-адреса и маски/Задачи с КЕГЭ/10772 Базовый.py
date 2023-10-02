from ipaddress import *


for mask in range(33):
    net = ip_network(f'117.184.113.45/{mask}', 0)
    print(net, net.netmask)
# 117.184.64.0/18 255.255.192.0
# 192
