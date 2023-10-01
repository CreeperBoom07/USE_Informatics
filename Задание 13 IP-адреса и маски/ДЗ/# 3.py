from ipaddress import *

for mask in range(33):
    net = ip_network(f'154.201.208.17/{mask}', 0)
    print(net, net.netmask)
##154.201.192.0/18 255.255.192.0
##154.201.192.0/19 255.255.224.0
# 224
