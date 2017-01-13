#!/usr/bin/python3.5.2/bin/python3.5

import socket,time,sys

s=socket.fromfd( sys.stdin.fileno(),socket.AF_INET,socket.SOCK_DGRAM )
message,address=s.recvfrom( 8192 )
s.connect( address )

for i in range( 10 ):
    rep="Reply %d: %s"%( i+1,message )
    brep=bytes( rep,encoding="utf-8" )
    #s.sendto( brep,address )
    #s.sendto( "Reply %d:%s"%( i+1,message ),address )
    #s.send( "Reply %d:%s"%( i+1,message ) )
    s.send( brep )
    time.sleep( 2 )

end="OK,I'm done sending replies.\n"
bend=bytes( end,encoding="utf-8" )
s.send( bend )

