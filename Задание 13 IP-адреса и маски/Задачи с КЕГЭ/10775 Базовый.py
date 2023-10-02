# 1 способ

from ipaddress import *

net = ip_network('156.128.0.227/255.255.255.248', 0)

ip1 = ip_address('156.128.0.227')
ip2 = ip_address('156.128.0.224')
print(int(ip1) - int(ip2))


# 2 способ
print('.'.join(f'{x:08b}' for x in [255, 255, 255, 248]))
print('.'.join(f'{x:08b}' for x in [156, 128, 0, 227]))
##11111111.11111111.11111111.11111|000
##10011100.10000000.00000000.11100|011
print(int('011', 2))

# 3
