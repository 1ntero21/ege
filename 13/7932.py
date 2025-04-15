from ipaddress import ip_network

net = ip_network('135.13.142.29/255.255.255.128', 0)

for i in net.hosts():
    print(i)

# 13513142126