#!/usr/bin/python3.5.2/bin/python3.5
#   basictitle.py

import html.parser
import sys

class TitleParser( html.parser.HTMLParser ):
    def __init__( self ):
        self.title=''
        self.readingtitle=0
        html.parser.HTMLParser.__init__( self )

    def handle_starttag( self,tag,attrs ):
        if 'title'==tag:
            self.readingtitle=1

    def handle_data( self,data ):
        if self.readingtitle:
            self.title+=data

    def handle_endtag( self,tag ):
        if 'title'==tag:
            self.readingtitle=0

    def gettitle( self ):
        return self.title

fd=open( sys.argv[1] )
tp=TitleParser(  )
tp.feed( fd.read(  ) )
print( "Title is:",tp.gettitle( ) )
