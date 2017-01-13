#!/usr/bin/python3.5.2/bin/python3.5
#   gethostbyaddr-paranoid.py

import sys,socket

def getipaddrs( hostname ):
    """Get a list of IP addresses from a given hostname.This is a standard( forward) lookup.""" 
    result=socket.getaddrinfo( hostname,None,0,socket.SOCK_STREAM )
    return [x[4][0] for x in result]

def gethostname( ipaddr ):
    """Get the hostname from a given IP address.This is a reverse lookup."""
    return socket.gethostbyaddr( ipaddr)[0]

try:
    hostname=gethostname( sys.argv[1] )
    ipaddrs=getipaddrs( hostname )
except socket.herror as e:
    print( "No host names available for %s;this may be normal."% sys.argv[1] )
    sys.exit( 0 )
except socket.gaierror as e:
    print( "Got hostname %s,but it could not be forward-resolved:%s"%( hostname,str( e ) ) )
    sys.exit( 0 )

if not sys.argv[1] in ipaddrs:
    print( "Got hostname %s,but on forward lookup,"%hostname )
    print( "Original IP %s did not appear in IP address list."%sys.argv[1] )
    sys.exit( 0 )

print( "Validated hostname:",hostname )
    
