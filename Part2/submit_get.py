#!/usr/bin/python3.5.2/bin/python3.5
#   submit_get.py
import sys,urllib.request,urllib.parse

def addGETdata( url,data ):
    return url+'?'+urllib.parse.urlencode( data )

zipcode=sys.argv[1]
url=addGETdata( 'http://www.wunderground.com/cgi-bin/findweather/getForecast',[( 'query',zipcode )])
print( "Using URL",url )
req=urllib.request.Request( url )
fd=urllib.request.urlopen( req )
while 1:
    data=fd.read( 1024 )
    if not len( data ):
        break
#    sys.stdout.write( data.decode( "utf-8" ) )

