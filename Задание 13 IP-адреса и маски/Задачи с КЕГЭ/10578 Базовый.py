from ipaddress import *



for mask in range(33):
    net1 = ip_network(f'10.96.180.231/{mask}', 0)
    net2 = ip_network(f'10.96.140.118/{mask}', 0)
    if net1 != net2:
        print(net1, net2)
# 13
