from ipaddress import *

for mask in range(33):
    net = ip_network(f'203.75.227.102/{mask}', 0)
    print(net, net.netmask)
#203.75.224.0/19 255.255.224.0
#203.75.224.0/20 255.255.240.0
#203.75.224.0/21 255.255.248.0
#203.75.224.0/22 255.255.252.0
# 4
