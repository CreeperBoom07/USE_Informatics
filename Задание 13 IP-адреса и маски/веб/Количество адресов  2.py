from ipaddress import *

for mask in range(33):
    net = ip_network(f'108.133.75.91/{mask}', 0)
    print(net, net.num_addresses)

## 108.133.75.64/26 64
## 108.133.75.64/27 32
## 64
