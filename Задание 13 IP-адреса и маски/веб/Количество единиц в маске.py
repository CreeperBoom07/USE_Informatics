from ipaddress import *

for mask in range(33):
    net = ip_network(f'148.195.140.28/{mask}', 0)
    print(net)
#148.195.140.0/22
#148.195.140.0/23
#148.195.140.0/24
#148.195.140.0/25
#148.195.140.0/26
#148.195.140.0/27
# => 22
