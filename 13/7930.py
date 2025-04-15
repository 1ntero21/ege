from ipaddress import ip_network

net = ip_network('83.152.68.115/255.255.224.0', 0)

for i in net.hosts():
    print(i)


# 8315295254