from socket import *
import random

BUFF_SIZE = 1024
port = 7777

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
box = [[]]

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    data = data.split()
    if random.randint(1, 10) <= 1: 
        continue
    
    if data[0] == 'send':
        box[data[1]].append(data[2])
    if data[0] == 'receive' :
        s_sock.sendto(box[data[1]][0].encode(), addr)