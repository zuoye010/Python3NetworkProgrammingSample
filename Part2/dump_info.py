#!/usr/bin/python3.5.2/bin/python3.5
#   dmup_info.py

import sys,urllib.request

req=urllib.request.Request( sys.argv[1] )
fd=urllib.request.urlopen( req )
print( "Retrieved",fd.geturl(  ) )
info=fd.info(  )
for key,value in info.items(  ):
    print( "%s=%s"%( key,value ) )
