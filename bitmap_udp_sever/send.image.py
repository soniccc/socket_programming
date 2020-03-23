#!/usr/bin/env python

from PIL import Image
import pickle
import socket
from time import sleep

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

image = Image.open("../../images/nat.bmp")

width, height = image.size
print(width, height)

for y in range(height):
    for x in range(width):
        pos = (x, y)
        rgba = image.getpixel(pos)
#       print(pos, rgba)
        message = (pos, rgba)
        data = pickle.dumps(message)
        udp_client.sendto(data, ("127.0.0.1", 20001))
        sleep(0.001)

    

