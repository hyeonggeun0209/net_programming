from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    filename = req[0].split(' ')[1].strip('/')
    
    if filename in os.listdir(os.getcwd()):
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        res = 'HTTP/1.1 200 OK\r\n' \
                'Content - Type: ' + mimeType + '\r\n' \
                '\r\n'
        data = f.read()
        if filename == 'index.html':
            c.send(res.encode() + data.encode('euc-kr'))
        else:
            c.send(res.encode() + data)
            
    else:
        res = 'HTTP/1.1 404 Not Found\r\n' \
                '\r\n' \
                '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' \
                '<BODY>Not Found</BODY></HTML>'
        c.send(res.encode())
        
    c.close()

