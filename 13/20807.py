from ipaddress import ip_network


count = 0
net = ip_network('172.16.192.0/255.255.192.0', 0)
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if ip.count('1') % 5 != 0:
        count += 1
print(count)