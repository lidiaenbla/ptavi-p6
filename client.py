#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

SIP = ""

try:
    METHOD = sys.argv[1]
    SIP_METHOD = sys.argv[2]
except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

PORT = int(SIP_METHOD.split(":", -1)[1])
SIP = "sip:" + SIP_METHOD.split(":", -1)[0] + " SIP/2.0\r\n"

if METHOD == "INVITE":
    LINE = "INVITE " + SIP
elif METHOD == "BYE":
    LINE = "BYE " + SIP

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect(('127.0.0.1', PORT))
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print(data.decode('utf-8'))
    data = data.decode('utf-8').split()
    if data[1] == "100" and data[4] == "180" and data[7] == "200":
        LINE = "ACK " + SIP
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')

print("Socket terminado.")
