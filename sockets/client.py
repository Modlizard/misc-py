import socket

host,port = '127.0.0.1',6353

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'18')
    data = s.recv(1024)

print('Server:', int.from_bytes(data, byteorder='big'))
#.replace('b','',1)
