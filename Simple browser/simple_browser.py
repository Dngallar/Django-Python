#!/usr/bin/env python3

"""
    Simplest Browser in Python

    Domingo Gallardo Saavedra
    August, 18 2020
"""

import socket

# End point to send and receive data to the computer
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('iowlabs.com' , 80)) # Call
# Data in the Internet is generally sent in UTF-8. In Pytho is Unicode
cmd = 'GET http://iowlabs.com/index.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) # Up to 512 characters
    if len(data) < 1:
        break
    print(data.decode(), end = '')

mysock.close()
