#!/usr/bin/python3.5.2/bin/python3.5

import sys

print ( "Welcome." )
print( "Please enter a string:" )
sys.stdout.flush( )
line=sys.stdin.readline( ).strip( )
print( "You entered %d characters."%len( line ) )
