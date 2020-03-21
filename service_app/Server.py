#!/usr/bin/env python3

# Author : Y. Achbar
# Original Script by B.Chahal
# Expanded the code to use a server class. So it can be reused for other
# TCP/UDP based applications

import socket


class Server(object):
    def __init__(self, Bind_addr, port):
        self.port = int(port)
        self.Bind_addr = str(Bind_addr)

    def tcp_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
            socket_tcp.bind((self.Bind_addr, self.port))
            socket_tcp.listen(5)
            connection, addr = socket_tcp.accept()
            return connection

    def receive_data(self, buffer_size, message):
        connection = self.tcp_socket()
        with connection:
           print('[*] Established connection')
           print(f"Connection to {self.Bind_addr}:{self.port} established")
           connection.send(bytes(str(message), "utf-8"))
           while True:
               data = connection.recv(buffer_size)
               if not data:
                   break
               else:
                   print('[*] Data received: {}'.format(data.decode('utf-8')))
               connection.send(data)

def main():
    try:
        HOST_IP = socket.gethostbyname(socket.gethostname())
    except Exception as e:
        print('Unable to get your local IP, You must be rich and using a MAC, 0.0.0.0 will be used for your server IP')
        HOST_IP = '0.0.0.0'

    PORT = 12345
    Myserver = Server(HOST_IP, PORT)
    BUFFER_SIZE = 1024
    ACK_message = 'You data has been received successfully! If you fall into  toilet roll hoarders category then leave that server alone and Fuck off !'
    Send = Myserver.receive_data(BUFFER_SIZE, ACK_message)

if __name__ == '__main__':
    main()
