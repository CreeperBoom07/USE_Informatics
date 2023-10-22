from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'112.117.107.70/{mask}', 0)
    net2 = ip_network(f'112.117.121.80/{mask}', 0)
    if net1 == net2:
        print(net1.num_addresses)
# 8192
