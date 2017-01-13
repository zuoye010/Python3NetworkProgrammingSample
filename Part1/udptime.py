#!/usr/bin/python3.5.2/bin/python3.5

import socket,sys,struct,time

host=sys.argv[1]
port=51423

s=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
s.sendto( ''.encode( 'utf-8' ),( host.encode('utf-8'),port ) )

print( "Looking for replies;press Ctrl-C or Ctrl-Break to stop." )
buf=s.recvfrom( 2048 )[0]
if 4!=len( buf ):
    print( "Wrong-sized reply %d:%s"%( len( buf ),buf ) )
    sys.exit( 1 )

secs=struct.unpack( "!I",buf )[0]
secs-=2208988800
print( time.ctime( int( secs ) ) )
