from ipaddress import ip_network


for m in range(0, 33):
    net1 = ip_network(f'200.154.190.12/{m}', 0)
    net2 = ip_network(f'200.154.184.0/{m}', 0)
    if str(net1) == str(net2):
        if '200.154.190.12' != str(net1.network_address) and '200.154.190.12' != str(net1.broadcast_address):
            if '200.154.184.0' != str(net2.network_address) and '200.154.184.0' != str(net2.broadcast_address):
                print(m)