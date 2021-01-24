#!/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

def portscanner():
    host = input("tell me ip address: ")
    port = int(input("port ? :"))
    # if s.connect return error
    # s.connect_ex() gives you return code, 0 for success , 1 for failed
    
    if s.connect_ex((host, port)):
        print("port closed")
    else:
        print("port open")

while True:
    portscanner()

