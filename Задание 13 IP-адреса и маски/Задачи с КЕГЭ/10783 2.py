from ipaddress import *
lst = []
for mask in range(33):
    net1 = ip_network(f'121.171.5.70/{mask}', 0)
    net2 = ip_network(f'121.171.5.107/{mask}', 0)
    if net1 == net2:
        lst.append(net1.num_addresses)
print(min(lst))
# 64
