from ipaddress import ip_network


count = 0
net = ip_network('172.16.80.0/255.255.248.0', 0)
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if ip.count('1') % 2 != 0:
        count += 1
print(count)