#!/usr/bin/python3.5.2/bin/python3.5
#   weather.py

import html.parser
import sys,re
import urllib.request,urllib.parse

interesting=['Pressure','Visibility','Clouds','Dew Point','Humidity','Rainfall','Snow Depth']

class WeatherParser( html.parser.HTMLParser ):
    def __init__( self ):
        self.taglevels=[]
        self.handledtags=['title','table','tr','td','th','span','a']
        self.processing=None
        self.interestingtable=0
        self.row=[]
        html.parser.HTMLParser.__init__( self )

    def handle_starttag( self,tag,attrs ):
        if len( self.taglevels ) and tag==self.taglevels[-1]:
            self.handle_endtag( tag )
        self.taglevels.append( tag )
        if 'br'==tag:
            self.handle_data( "<NEWLINE>" )
        elif tag in self.handledtags:
            self.data=''
            self.processing=tag

    def handle_data( self,data ):
        if self.processing:
            self.data+=data

    def handle_endtag( self,tag ):
        if not tag in self.taglevels:
            return

        while len( self.taglevels ):
            starttag=self.taglevels.pop(  )
            if starttag in self.handledtags:
                if len( self.data ):
                    self.finishprocessing( starttag )
            if starttag==tag:
                break
    
    def cleanse( self ):
        self.data=re.sub( '(\s|\xa0)+',' ',self.data )
        self.data=self.data.replace( '<NEWLINE>',"\n" ).strip(  )

    def finishprocessing( self,tag ):
        global interesting
        self.cleanse( )
        if 'title'==tag and tag==self.processing:
            print( " ***%s ***"%self.data )
        elif ( 'span'==tag ) and tag==self.processing:
            if 1==self.interestingtable:
                if len( self.data ):
                    self.row.append( self.data )
        elif ( 'td'==tag or 'th'==tag ) and tag==self.processing:
            for item in interesting:
                if re.search( item,self.data,re.I ):
                    self.interestingtable=1
                    interesting=[x for x in interesting if x!=item]
                    print( "\n ***%s   "%self.data.strip(),end="" )
                    break
            #        else:
             #           self.row.append( self.data )
        elif 'tr'==tag and self.interestingtable:
            self.writerow(  )
            self.row=[]
        elif 'table'==tag:
            self.interestingtable=0

        self.processing=None

    def writerow( self ):
        for myitem in self.row:
            sys.stdout.write( myitem )
        sys.stdout.write( "\n" )

    def handle_charref( self,name ):
        try:
            charnum=int( name )
        except ValueError:
            return

        if 1>charnum or 255<charnum:
            return

        self.handle_data( chr( charnum ) )

zipcode=input( "Enter ZIP code:" )
url="http://www.wunderground.com/cgi-bin/findweather/getForecast?query="+zipcode

req=urllib.request.Request( url )
fd=urllib.request.urlopen( req )

parser=WeatherParser(  )
data=fd.read(  ).decode( 'utf-8' )
#data=re.sub( r' ( [^=]+)=[^="]+="',' \\1="',data )
#data=re.sub( r'( ?s)<!--.*?-->','',data )
parser.feed( data )
    


