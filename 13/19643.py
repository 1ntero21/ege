from ipaddress import ip_network


net = ip_network('158.214.121.40/255.255.255.224', 0)
for i in net.hosts():
    print(i)
    break


# 15821412133