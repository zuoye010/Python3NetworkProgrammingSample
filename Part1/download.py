#!/usr/bin/python3.5.2/bin/python3.5

import urllib,sys

f=urllib.urlopen( sys.argv[1] )

while 1:
    buf=f.read( 2048 )
    if not len( buf ):
        break;
    sys.stdout.write( buf )
