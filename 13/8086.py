from ipaddress import ip_network

net = ip_network('143.168.72.213/255.255.255.240', 0)

for i in net.hosts():
    print(i)

#12316872222