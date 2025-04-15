from ipaddress import ip_network

net = ip_network('123.215.104.78/255.255.252.0', 0)

for i in net.hosts():
    print(i)

# 123215107254