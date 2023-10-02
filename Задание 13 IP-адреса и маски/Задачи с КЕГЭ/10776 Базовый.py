from ipaddress import *


for mask in range(33):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    print(net)
# 111.91.192.0/18
# 111.91.192.0/19
# 111.91.192.0/20
# 12
