from socket import *
import time

BUFF_SIZE = 1024
port = 7777

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))
t = 2
data = 'send [1] '
i = 0

c_sock.send(data.encode())

while True:
    c_sock.settimeout(t)
    try :
        r_data = c_sock.recv(BUFF_SIZE).decode()
        print(r_data)
    except timeout:
        if i != 3:
            c_sock.send(data.encode())
            i += 1
        else:
            break