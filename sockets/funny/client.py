import socket
import time

host,port = '127.0.0.1',6353

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    time.sleep(0.25)
    s.sendall(b'Fuck you')
    data = s.recv(1024)
    print('Server:', repr(data).replace('b','',1))
    while True:
        s.sendall(b'Fuck you')
        data = s.recv(1024)
        time.sleep(0.5)
        print('Server:', repr(data).replace('b','',1))
        time.sleep(0.5)
    
#.replace('b','',1)
