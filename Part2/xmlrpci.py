#!/usr/bin/python3.5.2/bin/python3.5
#   xmlrpcbasic.py

import xmlrpc.client

url='http://localhost:8088'

s=xmlrpc.client.ServerProxy( url )
print( "Gathering avilable methods..." )
methods=s.system.listMethods(  )
print( "result:"+catdata )
