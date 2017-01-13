#!/usr/bin/python3.5.2/bin/python3.5

import socket,sys

host=sys.argv[1]
textport=sys.argv[2]

s=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
try:
    port=int( textport )
except ValueError:
    port=socket.getservbyname( textport,'udp' )

s.connect( ( host,port ) )

print( "Enter data to transmit:" )
data=sys.stdin.readline(  ).strip(  )
s.sendto( data.encode( 'utf-8' ),( host,port ) )
#s.sendall( data.encode( 'utf-8' ) )
print( "Looking for replies;press Ctrl-C or Ctrl-Break to stop." )

while True:
#for i in range( 10 ):
    buf,address=s.recvfrom( 2048 )
    if not len( buf ):
        break
    sys.stdout.write( buf.decode( 'ascii' ) )
    print( "" )
#    print( "Get from",address  )
    continue
