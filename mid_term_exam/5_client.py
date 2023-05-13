from socket import *
import time

BUF_SIZE = 1024
LENGTH = 12

while True:
    num = input("input 1 or 2 or 3 or q: ")

    if num == '1':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8888))
        s.send(b'1')
        msg = s.recv(BUF_SIZE).decode().split()
        a = msg[0].encode()
        val = int.from_bytes(msg[0], 'big')
        print(msg[0], int(val))

    elif num == '2':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8888))
        s.send(b'2')
        msg = int.from_bytes(s.recv(BUF_SIZE).decode().split(),'big')
        print(msg)
    
    elif num == '3':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8888))
        s.send(b'3')
        msg = int.from_bytes(s.recv(BUF_SIZE).decode().split(),'big')
        print(msg)

    else:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8888))
        s.send(num.encode())
        s.recv(BUF_SIZE)
        s.close()

s.close()