#!/usr/bin/python3.5.2/bin/python3.5
#   environment.py

import sys,socket

def getipaddrs( hostname ):
    """Given a host name,perform a standard( forward ) lookup and return a list of IP addresses for that host."""
    result=socket.getaddrinfo( hostname,None,0,socket.SOCK_STREAM )
    return [x[4][0] for x in result]

hostname=socket.gethostname(  )
print( "Host name:",hostname  )

print( "Fully-qualified name:",socket.getfqdn( hostname ) )
try:
    print( "IP addresses:",", ".join( getipaddrs( hostname ) ) )
except socket.gaierror as e:
    print( "Couldn't not get IP addresses:",e )
