import socket
import binascii
import sys

ip = '220.69.189.125'
port = 443

name = socket.gethostbyaddr(ip)[0]
print(name)

proto = socket.getservbyport(port)
print(proto)

print('{}://{}'.format(proto,name))

packed = socket.inet_aton(ip)
print(packed)
