from ipaddress import *


for mask in range(33):
    net = ip_network(f'175.122.80.13/{mask}', 0)
    print(net, net.num_addresses)
##175.122.80.0/20 4096
##175.122.80.0/21 2048
##175.122.80.0/22 1024
##175.122.80.0/23 512
##175.122.80.0/24 256
##175.122.80.0/25 128
##175.122.80.0/26 64
# Ответ 7

