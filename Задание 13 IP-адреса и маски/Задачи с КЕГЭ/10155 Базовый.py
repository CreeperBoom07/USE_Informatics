from ipaddress import *


for mask in range(33):
    net = ip_network(f'142.198.113.106/{mask}', 0)
    print(net)
##142.198.112.0/20
##142.198.112.0/21
##142.198.112.0/22
##142.198.112.0/23
# 23
