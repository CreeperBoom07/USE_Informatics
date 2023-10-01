from ipaddress import *

# Формирем сеть, адрес узла указываем любой
net = ip_network('192.168.0.0/255.255.128.0', 0)

k = 0
for ip in net:
    # Числовое значение ip - адреса
    c = int(ip)
    if c % 4 == 0:
        k += 1
print(k)
# 8192
