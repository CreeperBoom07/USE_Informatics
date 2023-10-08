from ipaddress import *

net = ip_network('156.132.15.138/255.255.252.0', 0)
print(net)
# 156.132.12.0 - net address

ip1 = ip_address('156.132.15.138')
ip2 = ip_address('156.132.12.0')
print(int(ip1) - int(ip2))
# 906
