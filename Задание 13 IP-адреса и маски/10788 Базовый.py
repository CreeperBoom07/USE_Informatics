from ipaddress import *

def f(ip):
    ip = ip.rstrip('0123456789')
    ip = ip.rstrip('/')
    return '.'.join([f'{n:08b}' for n in map(int, ip.split('.'))])

k = 0
for mask in range(33):
    net1 = ip_network(f'201.44.240.33/{mask}', 0)
    net2 = ip_network(f'201.44.240.107/{mask}', 0)
    if net1 == net2:
        ip = f(str(net1))
        if ip.count('1') >= 5:
            k += 1
print(k)


