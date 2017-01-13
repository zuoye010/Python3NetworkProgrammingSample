#!/usr/bin/python3.5.2/bin/python3.5

import socket,traceback

host=''
port=51426

s=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
s.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR,1 )
s.setsockopt( socket.SOL_SOCKET,socket.SO_BROADCAST,1 )
s.bind( ( host,port ) )

while 1:
    try:
        message,address=s.recvfrom( 8192 )
        print( "Got data %s" %message.decode( "utf-8" ) )
        print( "Got data from",address )
        s.sendto( "I am here".encode( "utf-8" ),address )
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc(   )
