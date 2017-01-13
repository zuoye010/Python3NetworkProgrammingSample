#!/usr/bin/python3.5.2/bin/python3.5
#   xmlrpcbasic.py

import xmlrpc.client

url='http://localhost:8088'

s=xmlrpc.client.ServerProxy( url )
catdata=s.sayHello(  )
print( "result:"+catdata )
