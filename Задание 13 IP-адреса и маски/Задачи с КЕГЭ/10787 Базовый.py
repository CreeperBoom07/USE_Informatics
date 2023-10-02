from ipaddress import *

for mask in range(33):
    net = ip_network(f'111.24.160.159/{mask}', 0)
    print(net)
##111.24.160.128/25
##111.24.160.128/26
##111.24.160.128/27
# 27
