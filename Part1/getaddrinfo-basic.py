#!/usr/bin/python3.5.2/bin/python3.5
#   getaddrinfo-basic.py

import sys,socket

result=socket.getaddrinfo( sys.argv[1],None )

for data in result:
    print( data[4] )
