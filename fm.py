#
# craig smith - july 8, 2020
#

a = {'a': {'PublicKey': 'a/key=', 'AllowedIPs': '10.1.0.1/16', 'Endpoint': '1.1.1.1:7000'},
     'b': {'PublicKey': 'b/key=', 'AllowedIPs': '10.2.0.1/16', 'Endpoint': '2.2.2.2:7000'},
     'c': {'PublicKey': 'c/key=', 'AllowedIPs': '10.3.0.1/16', 'Endpoint': '3.3.3.3:7000'},
     'd': {'PublicKey': 'e/key=', 'AllowedIPs': '10.4.0.1/16', 'Endpoint': '4.4.4.4:7000'}}

l = []

for x in a.keys():
    for y in a.keys():
        if x == y:
            pass
        else:
            if (x + y) and (y + x) not in l:
                l.append(x + y)

for e in a.keys():
    print('Server: ', e)
    for h in l:
        if e in h:
            print(a[(h.replace(e, ''))])

