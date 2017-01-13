#!/usr/bin/python3.5.2/bin/python3.5

import sys,os,stat

new='#!/usr/bin/python3.5.2/bin/python3.5\n'
defaultPath='/home/ml/work/Net/'

print( 'Input file name' )
filename=sys.stdin.readline( )[:-1]

absoluteFileName=defaultPath+filename

f=open(absoluteFileName,'w' )

f.write( new )
f.write( '#   '+filename+'\n\n' )

f.close()

os.chmod( absoluteFileName,stat.S_IRWXO|stat.S_IRWXG|stat.S_IRWXU )

os.system( "vim "+absoluteFileName+' +3' )




