#!/usr/bin/python3.5.2/bin/python3.5
#   error_basic.py

import sys,urllib.request

req=urllib.request.Request( sys.argv[1] )

try:
    fd=urllib.request.urlopen( req )
except urllib.error.URLError as e:
    print( "Error retrieving data:",e )
    sys.exit( 1 )

print( "Retrieved",fd.geturl( ) )
info=fd.info(  )
for key,value in info.items(  ):
    print( "%s=%s"%( key,value ) )
