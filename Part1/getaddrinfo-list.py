#!/usr/bin/python3.5.2/bin/python3.5
#   getaddrinfo-basic.py

import sys,socket

result=socket.getaddrinfo( sys.argv[1],None,0,socket.SOCK_STREAM )

counter=0
for data in result:
    print( "%-2d: %s"%(counter,data[4] ) )
    counter+=1
