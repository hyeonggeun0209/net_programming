from socket import *
import time

BUFF_SIZE = 1024
port = 7777

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))
t = 1
data = 'ping'
RTT = 0 
i = 0

c_sock.send(data.encode())
s_time = time.time()

while RTT == 0:
    c_sock.settimeout(t)
    try :
        r_data = c_sock.recv(BUFF_SIZE).decode()
        r_time = time.time()
        RTT = r_time - s_time
        print(f"Success (RTT: {RTT})")
    except timeout:
        if i != 2:
            c_sock.send(data.encode())
            i += 1
        else:
            break
if RTT == 0: print("Fail")