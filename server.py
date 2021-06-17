import socket

host,port = '127.0.0.1',6353

def process(data):
    data = (int(data)**2).to_bytes(10, byteorder='big')
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    print('Running....')
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(process(data))
