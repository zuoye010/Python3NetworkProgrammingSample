#!/usr/bin/python3.5.2/bin/python3.5

import sys,os

new='#!/usr/bin/python3.5.2/bin/python3.5\n\n'

for filename in os.listdir( r'/home/ml/work/Net' ):
    f=open( filename,'r' )
    line=f.readline( )
    if line==new:
        f.close(  )
        continue
    else:
       Lines=f.readlines(  ) 
       f.close(  )
       Lines[0]=new
       f=open( filename,'w' )
       f.truncate(  )
       for newline in Lines:
           f.write( newline )
       f.close(  )



