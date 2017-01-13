#!/usr/bin/python3.5.2/bin/python3.5
#   xmlrpcserver.py

import xmlrpc.server

class MyObject:
    def sayHello( self ):
        return "Hello xmlrpc"

obj=MyObject(  )
server=xmlrpc.server.SimpleXMLRPCServer( ("localhost",8088) )
server.register_instance( obj )

print( "Listening on port 8088" )
server.serve_forever(  )
