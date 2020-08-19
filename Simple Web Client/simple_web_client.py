#!/usr/bin/env python3

"""
    Simple Web Client

    Domingo Gallardo Saavedra
    August, 18 2020
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# localhost -> 127.0.0.1
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/file.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = '')

mysock.close()
