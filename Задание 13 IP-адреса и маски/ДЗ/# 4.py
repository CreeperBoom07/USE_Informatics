from ipaddress import *

for mask in range(33):
    net = ip_network(f'122.21.49.91/{mask}', 0)
    print(net)
##122.21.48.0/20
##122.21.48.0/21
##122.21.48.0/22
##122.21.48.0/23
# 20
