#!/usr/bin/python3.5.2/bin/python3.5
#   getfile.py

import ftplib
import datetime

begin=datetime.datetime.now( )
ftp=ftplib.FTP( "192.168.0.159" )
ftp.login( "dyl","282" )
filename="File_0"
filed=open( filename,'wb' )
ftp.retrbinary( 'RETR File_0',filed.write,1024 )
filed.close( )
ftp.close( )
end=datetime.datetime.now( )
used=(end-begin).microseconds/1000.0
print( used )
