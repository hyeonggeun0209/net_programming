from socket import *
import time

BUF_SIZE = 1024
LENGTH = 4

try:
    f = open('data.txt', 'r')

except:
    f = open('data.txt', 'w')

f.close()

while True:
    num = input("input 1 or 2 or q: ")

    if num == '1':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8000))
        s.send(b'Request')
        msg = s.recv(BUF_SIZE).decode().split()
        text = f"{time.asctime()}: Device1: Temp={msg[0]}, Humid={msg[1]}, Lilum={msg[2]}\n"

    elif num == '2':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',9000))
        s.send(b'Request')
        msg = s.recv(BUF_SIZE).decode().split()
        text = f"{time.asctime()}: Device2: Heartbeat={msg[0]}, Steps={msg[1]}, Cal={msg[2]}\n"
    
    else:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8000))
        s.send(num.encode())
        s.recv(BUF_SIZE)
        s.close()

        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',9000))
        s.send(num.encode())
        s.recv(BUF_SIZE)
        s.close()
        break
    
    f = open('data.txt', 'a', encoding='utf-8')
    f.write(text)
    f.close()
    s.close()
s.close()