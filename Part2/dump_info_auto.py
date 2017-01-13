#!/usr/bin/python3.5.2/bin/python3.5
#   dump_info_auto.py

import sys,urllib.request,getpass

class TerminalPassword( urllib.request.HTTPPasswordMgr ):
    def find_user_password( self,realm,authuri ):
        retval=urllib.request.HTTPPasswordMgr.find_user_password( self,realm,authuri )

        if  None==retval[0] and None==retval[1]:
            sys.stdout.write( "Login required for %s at %s\n" %( realm,authuri ) )
            sys.stdout.write( "Username:" )
            username=sys.stdin.readline(  ).rstrip(  )
            password=getpass.getpass(  ).rstrip(  )
            return ( username,password )
        else:
            return retval

req=urllib.request.Request( sys.argv[1] )
opener=urllib.request.build_opener( urllib.request.HTTPBasicAuthHandler( TerminalPassword( ) ) )
fd=opener.open( req  )
print( "Retrieved",fd.geturl(  ) )
info = fd.info(  )

for key,value in info.items(  ):
    print( "%s=%s"%( key,value ) )
