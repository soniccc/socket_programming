#!/usr/bin/env python3

# Auhor: B Chahal

# This is a generic UDP server

import socket


def udp_serv():
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(("0.0.0.0", 20001))

    data, client_address = udp_server.recvfrom(1024)
    udp_server.sendto(data, client_address)


if __name__== "__main__":
    udp_serv()


