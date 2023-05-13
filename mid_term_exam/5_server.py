from socket import *
import random

BUF_SIZE = 1024
LENGTH = 12
port = 8888

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE).decode()

    temp = 0
    humid = 0
    lilum =  0

    if msg == '1':
        temp = random.randrange(0, 50)

    if msg == '2':
        humid = random.randrange(0, 100)

    if msg == '3':
        lilum = random.randrange(1, 150)
    
    print(temp,humid,lilum)
    temp = str(temp.to_bytes(4,'big'))
    humid = str(humid.to_bytes(4,'big'))
    lilum = str(lilum.to_bytes(4,'big'))
    text = temp + ' ' + humid + ' ' + lilum
    print(text)
    conn.send(text.encode())
    conn.close()
conn.close()
