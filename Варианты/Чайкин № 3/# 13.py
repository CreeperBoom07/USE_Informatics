from ipaddress import *

for x in range(0, 256):
    # bit = f'{x:08b}'
    try:
        net = ip_network(f'51.50.135.169/255.255.255.{x}', 0)
        print(net, x)
        
    except:
        continue
# 248
