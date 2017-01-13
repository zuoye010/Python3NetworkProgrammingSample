#!/usr/bin/python3.5.2/bin/python3.5
#   nbo.py

import struct,sys

def htons( num ):
    return struct.pack( '!H',num )

def htonl( num ):
    return struct.pack( '!I',num )

def ntohs( data ):
    return struct.unpack( '!H',data )[0]

def ntohl( data ):
    return struct.unpack( '!I',data )[0]

def sendstring( data ):
    return htonl( len( data ) ).decode( "utf-8" )+data
#    sdata1=data1.decode( "utf-8" )
 #   sdata=sdata1+data
  #  return sdata

print( "Enter a string:" )
str=sys.stdin.readline(  ).rstrip(  )


print( repr( sendstring( str ) ) )
