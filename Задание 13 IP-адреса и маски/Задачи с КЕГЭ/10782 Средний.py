from ipaddress import *

print('.'.join(f'{x:08b}' for x in [118,187,59,255]))
print('.'.join(f'{x:08b}' for x in [118,187,65,115]))


for mask in range(33):
    net1 = ip_network(f'118.187.59.255/{mask}', 0)
    net2 = ip_network(f'118.187.65.115/{mask}', 0)
    if net1 != net2:
        print(mask)
