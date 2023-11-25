from ipaddress import *

for a in range(0, 256):
    node = f'154.127.{a}.230'
    net = ip_network(f'{node}/255.255.255.192', 0)
    for ip in net:
        b = f'{ip:b}'
        if b[:16].count('1') > b[16:].count('1'):
            pass
        else:
            break
    else:
        print(a)

# 192
