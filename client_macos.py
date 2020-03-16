#!/usr/bin/env python3

# Author : B.Chahal
# For some reason socket.gethostbyname(socket.gethostname())
# does not return the host loopback address with python on MacOs.

import socket

HOST = '127.0.0.1'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)
    while True:
        data = client_sock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    client_sock.close()
