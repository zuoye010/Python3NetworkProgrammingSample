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

    def handle_entityref( self,name ):
        if html.parser.entitydefs.has_key( name ):
            self.handle_data( entitydefs[name] )
        else:
            self.handle_data( '&'+name+';' )

    def handle_charref( self,name ):
        try:
            charnum=int( name )
        except ValueError:
            return
        if 1>charnum or 255<charnum:
            return

        self.handle_data( chr( charnum ) )

    def gettitle( self ):
        return self.title

fd=open( sys.argv[1] )
tp=TitleParser(  )
tp.feed( fd.read(  ) )
print( "Title is:",tp.gettitle( ) )
