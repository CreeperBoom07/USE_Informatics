from ipaddress import *

# перебираем единицы в маске
for mask in range(33):
    net = ip_network(f'220.128.112.142/{mask}', 0)
    print(net, net.netmask)
# 255.255.224.0
# Ответ 224
