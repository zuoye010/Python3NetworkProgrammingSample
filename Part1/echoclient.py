#!/usr/bin/python3.5.2/bin/python3.5
#   echoclient.py

import socket,sys
port=51426
host='localhost'

data="x"*10*1024*1024

s=socket.socket( socket.AF_INET,socket.SOCK_STREAM )
s.connect( ( host,port ) )

byteswritten=0

while byteswritten<len( data ):
    startpos=byteswritten
    endpos=min( byteswritten+1024,len( data ) )
    mydata=data[startpos:endpos]
    bmydata=bytes( mydata,encoding="utf-8" )
    #byteswritten+=s.send( data[startpos:endpos] )
    byteswritten+=s.send( bmydata )
    sys.stdout.write( "Wrote %d bytes\r"%byteswritten )
    sys.stdout.flush(  )

s.shutdown( 1 )

print( "All data sent." )
while 1:
    buf=s.recv( 1024 )
    if not len( buf ):
        break
    sys.stdout.write( buf )
