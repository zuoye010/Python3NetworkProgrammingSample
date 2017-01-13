#!/usr/bin/python3.5.2/bin/python3.5

import socket
solist=[x for x in dir( socket ) if x.startswith( 'SO_' )]
solist.sort(  )
for x in solist:
    print x
