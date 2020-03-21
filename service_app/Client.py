#!/usr/bin/env python3

# Author : Y. Achbar
# Original Script by B.Chahal
# Expanded the code to use a client class. So it can be reused for other
# TCP/UDP based applications

import socket

class Client(object):
    def __init__(self, addr):
        self.addr = addr

    def _sock(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(self.addr)
        return client_sock

    def _get_data(self, buffer_size):
        #s = self._sock()
        s = self._sock()
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            return data.decode('utf-8') 
        s.close()

def main():
    #HOST = socket.gethostname()
    try:
        HOST_IP = socket.gethostbyname(socket.gethostname())
    except Exception as e:
        print('Unable to get your local IP, You must be rich and using a MAC, 0.0.0.0 will be used for your server IP')
        HOST_IP = '0.0.0.0'
    PORT = 12345
    BUFSIZ = 1024
    ADDR = (HOST_IP, PORT)
    c = Client(ADDR)
    data = c._get_data(BUFSIZ)
    print(data)

if __name__ == '__main__':
    main()
