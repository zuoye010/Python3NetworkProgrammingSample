#!/usr/bin/python3.5.2/bin/python3.5
#   dump_page.py
import sys,urllib.request

req=urllib.request.Request( sys.argv[1] )
fd=urllib.request.urlopen( req )
while 1:
    data=fd.read( 1024 )
    if not len( data ):
        break
    sdata=data.decode( "utf-8" )
    sys.stdout.write( sdata )
