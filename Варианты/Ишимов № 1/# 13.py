from ipaddress import *

net = ip_network('192.168.31.80/255.255.255.240')
m = 0
for ip in net:
    b = f'{ip:b}'
    m = max(m, b.count('1'))
print(m)
# 16
