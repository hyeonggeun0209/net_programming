from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

s.send(b'Hello')

msg = s.recv(BUF_SIZE)
if not msg:
    s.close()
    sys.exit()
elif msg != b'Filename':
    print('server:', msg.decode())
    s.close()
    sys.exit()
else:
    print('server:')