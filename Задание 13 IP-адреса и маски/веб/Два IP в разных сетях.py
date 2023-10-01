from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'157.127.182.76/{mask}', 0)
    net2 = ip_network(f'157.127.190.80/{mask}', 0)
    if net1 != net2:
        print(net1)
## 21
    
