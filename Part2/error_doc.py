#!/usr/bin/python3.5.2/bin/python3.5
#   error_basic.py

import sys,urllib.request

req=urllib.request.Request( sys.argv[1] )

try:
    fd=urllib.request.urlopen( req )
except urllib.error.HTTPError as e:
    print( "Error retrieving data:",e )
    print( "Server error document follows:\n" )
    print( e.read(  ) )
    sys.exit( 1 )
except urllib.error.URLError as e:
    print( "Error retrieving data:",e )
    sys.exit( 2 )

print( "Retrieved",fd.geturl( ) )
info=fd.info(  )
for key,value in info.items(  ):
    print( "%s=%s"%( key,value ) )
