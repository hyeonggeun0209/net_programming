from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE).decode()

    if msg == 'q':
        break
    else:
        hb = random.randrange(40, 140)
        walk = random.randrange(2000, 6000)
        cal = random.randrange(1000, 4000)
        text = f"{hb} {walk} {cal}"
        conn.send(text.encode())
        conn.close()
    
conn.close()