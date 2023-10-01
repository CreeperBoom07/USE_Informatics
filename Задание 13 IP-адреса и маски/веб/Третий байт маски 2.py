from ipaddress import *

for mask in range(33):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    print(net, net.netmask)
# 111.81.192.0/18 255.255.192.0
# 192
