#!/usr/bin/python3.5.2/bin/python3.5

import socket,traceback

host=''
port=51420

s=socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
s.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR,1 )
s.bind( ( host,port ) )

while 1:
    try:
        print( "Begin:" )
        message,address=s.recvfrom( 8192 )
        print( "Got data from",address )
        print( "Message is %s"%message )
        s.sendto( message,address )
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc(   )
