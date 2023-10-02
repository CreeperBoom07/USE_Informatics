from ipaddress import *

for mask in range(33):
    net = ip_network(f'191.173.145.240/{mask}', 0)
    print(net, net.num_addresses)
##191.173.144.0/20 4096
##191.173.144.0/21 2048
##191.173.144.0/22 1024
##191.173.144.0/23 512
# 512
