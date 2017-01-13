#!/usr/bin/python3.5.2/bin/python3.5
#   domparsesample.py

from xml.dom.minidom import parse,Node
import re,textwrap

class SampleScanner:
    def __init__( self,doc ):
        for child in doc.childNodes:
            if Node.ELEMENT_NODE==child.nodeType and 'book'==child.tagName:
                self.handleBook( child )

    def gettext( self,nodelist ):
        retlist=[]
        for node in nodelist:
            if Node.TEXT_NODE==node.nodeType:
                retlist.append( node.wholeText )
            elif node.hasChildNodes:
                retlist.append( self.gettext( node.childNodes ) )
        return re.sub( '\s+',' ',''.join( retlist ) )

    def handleBook( self,node ):
        for child in node.childNodes:
            if Node.ELEMENT_NODE!=child.nodeType:
                continue
            if 'title'==child.tagName:
                print( "Book title is:",self.gettext( child.childNodes ) )
            if 'author'==child.tagName:
                self.handleAuthor( child )
            if 'chapter'==child.tagName:
                self.handleChapter( child )

    def handleAuthor( self,node ):
        for child in node.childNodes:
            if Node.ELEMENT_NODE!=child.nodeType:
                continue
            elif 'name'==child.tagName:
                self.handleAuthorName( child )
            elif 'affiliation'==child.tagName:
                print( "Author affiliation:",self.gettext( [child]) )

    def  handleAuthorName( self,node ):
        surname=self.gettext( node.getElementsByTagName( "last" ) )
        givenname=self.gettext( node.getElementsByTagName( "first" ) )
        print( "Author Name: %s, %s"%( surname,givenname ) )

    def handleChapter( self,node ):
        print( "***Start of Chapter %s:%s"%( node.getAttribute( 'number' ),self.gettext( node.getElementsByTagName( 'title' ) ) ) )
        for child in node.childNodes:
            if Node.ELEMENT_NODE!=child.nodeType:
                continue
            if 'para'==child.tagName:
                self.handlePara( child )
    
    def handlePara( self,node ):
        paratext=self.gettext( [node] )
        paratext=textwrap.fill( paratext )
        print( paratext )
        print(   )

doc=parse( "/home/ml/work/Net/sample.xml" )
SampleScanner( doc )
