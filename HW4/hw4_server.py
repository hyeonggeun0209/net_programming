from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        try:
            rsp = data.decode()
        except:
            client.send(b'Try again')
        else:
            ans = round(eval(rsp),1)
            client.send(str(ans).encode())
    
    client.close()