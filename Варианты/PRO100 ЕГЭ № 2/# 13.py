from ipaddress import *

for mask in range(33):
    net = ip_network(f'111.81.27.224/{mask}', 0)
    print(net, net.netmask)
# 111.81.27.192/26 255.255.255.192
# 192
