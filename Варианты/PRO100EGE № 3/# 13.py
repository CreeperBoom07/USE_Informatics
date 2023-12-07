from ipaddress import *

net = ip_network('142.68.56.0/255.255.255.240')
k = 0
for ip in net:
    b = f'{ip:b}'
    if b[:16].count('1') < b[16:].count('1'):
        k += 1
print(k)
# 1
