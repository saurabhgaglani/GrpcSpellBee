import socket

HOST = 'localhost'
PORT = 64000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print("**************SOCKET LISTENING**************")
    conn, addr = sock.accept()
    with conn:
        print('Connected from: ', addr)
        while True:
            data = conn.recv(512)
            print(data)
            if not data:
                break
            conn.sendall(data)