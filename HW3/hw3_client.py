import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
name = 'Hyeonggeun Ji'.encode()
sock.send(name)
num = sock.recv(1024)
print(int.from_bytes(num,  'big'))
sock.close()