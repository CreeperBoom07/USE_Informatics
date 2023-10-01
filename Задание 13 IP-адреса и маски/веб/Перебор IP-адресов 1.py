from ipaddress import *

# сеть и маска
net = ip_network('184.178.54.144/255.255.255.240')

k = 0
for ip in net:
    # python 3.9+
    # f'{ip:b}' - переводим в двоичную с/с из 10-ричной
    b = f'{ip:b}'

    # для версии старше
    # b = bin(int(ip))[2:].zfill(32)
    if '111' in b:
        k += 1
print(k)
# 16
