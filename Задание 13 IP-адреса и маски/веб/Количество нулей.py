from ipaddress import *

for mask in range(33):
    net = ip_network(f'241.185.253.57/{mask}', 0)
    print(net)
# 241.185.252.0/22
# 241.185.252.0/23
# 32 - 23 = 9
