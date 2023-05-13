from socket import *
import random

BUFF_SIZE = 1024
port = 7777

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    if random.randint(1, 10) <= 4: 
        continue
    s_sock.sendto('pong'.encode(), addr)