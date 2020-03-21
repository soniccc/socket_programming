#!/usr/bin/env python3


# Author: B Chahal
# This script creates an UDP client


import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 20001
BUFSIZ = 1024
ADDR = (HOST, PORT)
message = "HELLO SERVER FROM CLIENT!"
data = message.encode()

def udp_clnt():
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("The Client Socket is UP!")

    udp_client_socket.sendto(data, ADDR)

    server_data, server_address = udp_client_socket.recvfrom(BUFSIZ)
    server_message = server_data.decode()
    print(server_message)

if __name__=='__main__':
    udp_clnt()
