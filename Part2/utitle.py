#!/usr/bin/python3.5.2/bin/python3.5
#   basictitle.py

import html.parser
import sys,re

class TitleParser( html.parser.HTMLParser ):
    def __init__( self ):
        self.taglevels=[]
        self.handledtags=['title','ul','li']
        self.processing=None
        html.parser.HTMLParser.__init__( self )

    def handle_starttag( self,tag,attrs ):
        if len( self.taglevels ) and tag==self.taglevels[-1]:
            self.handle_endtag( tag )
        self.taglevels.append( tag )

        if tag in self.handledtags:
            self.data=''
            self.processing=tag
            if 'ul'==tag:
                print( "List started." )

    def handle_data( self,data ):
        if self.processing:
            self.data+=data

    def handle_endtag( self,tag ):
        if not tag in self.taglevels:
            return
        while len( self.taglevels ):
            starttag=self.taglevels.pop(  )

            if starttag in self.handledtags:
                self.finishprocessing( starttag )

            if tag==starttag:
                break

    def cleanse( self ):
        self.data=re.sub( '\s+',' ',self.data )

    def finishprocessing( self,tag ):
        self.cleanse(  )
        if 'title'==tag and self.processing==tag:
            print( "Document Title:",self.data )
        elif 'ul'==tag:
            print( "List ended." )
        elif 'li'==tag and tag==self.processing:
            print( "List item:",self.data )
        self.processing=None

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
