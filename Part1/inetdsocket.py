#!usr/bin/python3.5.2/bin/python3.5

import sys,socket,time

s=socket.fromfd( sys.stdin.fileno(),socket.AF_INET,socket.SOCK_STREAM )

wel="Welcome.\n"
bwel=bytes( wel,encoding="utf-8" )
s.sendall( bwel )

acco="According to our records,you are connected from %s.\n"%str( s.getpeername() )
bacco=bytes( acco,encoding="utf-8" )
s.sendall( bacco )

localtime="The local time is %s.\n"%time.asctime()
blocaltime=bytes( localtime,encoding="utf-8" )
s.sendall( blocaltime )

