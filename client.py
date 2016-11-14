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
if METHOD == "INVITE":
    PORT = SIP_METHOD.split(":", -1)[1]
    SIP = SIP_METHOD.split(":", -1)[0]
    SERVER = SIP.split("@")[1]
    SIP = "sip:" + SIP + " SIP/2.0\r\n"
    LINE = "INVITE " + SIP + "\r\n"
elif METHOD == "BYE":

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
