#
# craig smith - july 8, 2020
#

peers = {1: {'PublicKey': 'a/key=', 'AllowedIPs': '10.1.0.1/16', 'Endpoint': '1.1.1.1:7000'},
         2: {'PublicKey': 'b/key=', 'AllowedIPs': '10.2.0.1/16', 'Endpoint': '2.2.2.2:7000'},
         3: {'PublicKey': 'c/key=', 'AllowedIPs': '10.3.0.1/16', 'Endpoint': '3.3.3.3:7000'},
         4: {'PublicKey': 'd/key=', 'AllowedIPs': '10.4.0.1/16', 'Endpoint': '4.4.4.4:7000'}}

l = []

for x in peers.keys():
    for y in peers.keys():
        if x == y:
            pass
        else:
            if (x, y) and (y, x) not in l:
                l.append((x, y))

print(l)

for each in peers.keys():
    print('Server: ', each)
    for e in l:
        x, y = e
        if x == each:
            print(peers[y])
        elif y == each:
            print(peers[x])
