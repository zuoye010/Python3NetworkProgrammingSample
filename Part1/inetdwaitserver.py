#!/usr/bin/python3.5.2/bin/python3.5
#   inetdwaitserver.py

import socket,time,sys,os

s=socket.fromfd( sys.stdin.fileno(),socket.AF_INET,socket.SOCK_DGRAM )
message,address=s.recvfrom( 8192 )
localaddr=s.getsockname(  )
s.close(  )

pid=os.fork(   )
if pid:
    sys.exit( 0  )

s2=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
s2.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR,1 )
s2.bind( localaddr )
s2.connect( address )

for i in range( 10 ):
    rep="wait Reply %d:%s"%( i+1,message)
    brep=bytes( rep,encoding="utf-8" )
    s2.send( brep)
    time.sleep( 2  )
end= "OK,I'm done sending replies.\n" 
bend=bytes( end,encoding="utf-8" )
s2.send( bend )
