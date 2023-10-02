from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240')

k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('0') > 21:
        k += 1
print(k)
