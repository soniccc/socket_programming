#!/usr/bin/env python3

# Author : B.Chahal
# For some reason socket.gethostbyname(socket.gethostname())
# does not return the host loopback address with python on MacOs.

import socket


HOST_IP = '127.0.0.1'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST_IP, PORT)

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.bind(ADDR)
        socket_tcp.listen(5)
        connection, addr = socket_tcp.accept()
        with connection:
            print('[*] Established connection')
            print(f"Connection to {addr} established")
            connection.send(bytes("Socket Programming in Python", "utf-8"))
            while True:
                data = connection.recv(BUFSIZ)
                if not data:
                    break
                else:
                    print('[*] Data received: {}'.format(data.decode('utf-8')))
                connection.send(data)
