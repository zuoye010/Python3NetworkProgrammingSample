#!/usr/bin/python3.5.2/bin/python3.5

import socket,sys

dest=( '<broadcast>',51426 )

s=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
s.setsockopt( socket.SOL_SOCKET,socket.SO_BROADCAST,1 )
s.sendto( "Hello".encode( "utf-8" ),dest )

print( "Looking for replies;press Ctrl-C to stop." )

while 1:
        (buf,address)=s.recvfrom( 2048 )
        if not len( buf ):
            break
        print( "Received from %s: %s"%(address,buf) )
