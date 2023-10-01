from ipaddress import *

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', 0)
    print(net)
##173.103.24.0/21
##173.103.24.0/22
##173.103.24.0/23
# 32 - 21 = 11
# 11
