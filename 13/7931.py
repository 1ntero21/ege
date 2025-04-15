from ipaddress import ip_network

net = ip_network('98.112.180.225/255.255.240.0', 0)

for i in net.hosts():
    print(i)


# 98112191254