#!/usr/bin/python3.5.2/bin/python3.5
#   error_all.py

import sys,socket
import urllib.request,urllib.error

req=urllib.request.Request( sys.argv[1] )

try:
    fd=urllib.request.urlopen( req )
except urllib.error.HTTPError as e:
    print( "Error retrieving data:",e )
    print( "Server error document follows:\n" )
    print( e.read(  ) )
    sys.exit( 1 )
except urllib.URLError as e:
    print( "Error retrieving data:",e )
    sys.exit( 2 )

print( "Retrieved",fd.geturl(  ) )

bytesread=0

while 1:
    try:
        data=fd.read( 1024 )
    except socket.error as e:
        print( "Error reading data:",e )
        sys.exit( 3 )

    if not len( data ):
        break
    bytesread+=len( data )
    sys.stdout.write( data.decode( 'utf-8' ) )

if fd.inof(  ).has_key( 'Content-Length' ) and long( fd.info(  )['Content-Length']) !=long( bytesread ):
    print( "Expected a document of size %d,but read %d bytes"%( long(fd.info()['Content-Length']),bytesread ) )
    sys.exit( 4 )
