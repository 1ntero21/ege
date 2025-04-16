from ipaddress import ip_network


count = 0
net = ip_network('5.2.5.0/255.255.0.0', 0)
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if ip.count('0') == 25:
        count += 1
print(count)