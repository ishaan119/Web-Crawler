'''
Created on Sep 7, 2013

@author: ishaansutaria
'''
import urllib, htmllib, re, sys, formatter

url = 'search.yahoo.com/search?p=internet+of+things&fr='
website = urllib.urlopen("http://"+url)
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
links =[]
links = ptext.anchorlist
for link in links:
    if re.search('http',link):
        print link
        website = urllib.urlopen(link)
        data = website.read()
        website.close()
        format = formatter.AbstractFormatter(formatter.NullWriter())
        ptext = htmllib.HTMLParser(format)
        ptext.feed(data)
        morelinks =[]
        morelinks = ptext.anchorlist
        for morelink in morelinks:
            if re.search('http',morelink):
                print morelink
                