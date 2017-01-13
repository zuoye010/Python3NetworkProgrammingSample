#!/usr/bin/python3.5.2/bin/python3.5
#   submit_get.py
import sys,urllib.request,urllib.parse

zipcode=sys.argv[1]
url='https://www.baidu.com/s'
value={'wd':zipcode}
postdata=urllib.parse.urlencode( value ).encode( 'ascii' )
req=urllib.request.Request( url,postdata)
with urllib.request.urlopen( req ) as fd:
    while 1:
        data=fd.read( 1024 )
        if not len( data ):
            break
        sys.stdout.write( data.decode( "utf-8" ) )
