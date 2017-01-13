#!/usr/bin/python3.5.2/bin/python3.5
#   domtree.py

from xml.dom.minidom import parse,Node

def scanNode( node,level=0 ):
    msg=node.__class__.__name__
    if Node.ELEMENT_NODE==node.nodeType:
        msg+=", tag: "+node.tagName
    print( " "*level*4,msg )
    if node.hasChildNodes:
        for child in node.childNodes:
            scanNode( child,level+1 )

doc=parse( '/home/ml/work/Net/sample.xml' )
scanNode( doc )
