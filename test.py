'''
Created on Sep 7, 2013

@author: ishaansutaria
'''
import urllib, htmllib, re, sys, formatter

url = 'www.aylanetworks.com'
website = urllib.urlopen("http://"+url)
data = website.read()
website.close()
hashLinks = {}
format1 = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format1)
ptext.feed(data)
links =[]
links = ptext.anchorlist
count = 0
links = list(set(links))    
print 'Number of links found on page one ' + str(len(links))
for link in links:
    if re.search('http',link) != None:
        hashLinks[link] = 1
        website = urllib.urlopen(link)
        data = website.read()
        website.close()
        forr = formatter.AbstractFormatter(formatter.NullWriter())
        pptext = htmllib.HTMLParser(forr)
        pptext.feed(data)
        subLinks = []
        subLinks = pptext.anchorlist
        subLinks = list(set(subLinks))
        for subLink in subLinks:
            if subLink in hashLinks.keys():
                subLinks.remove(subLink)
            else:
                hashLinks[subLink] = 1
    elif re.search('https',link) != None:
        print '*****  HTTPS Found' + link
    else:
        print 'Nothinf done' + link
    count = count + 1
count1 = 0    
for link in hashLinks:
    if re.search('ayla',link) != None:
        count1 = count1 + 1
        try:
            print link
            website = urllib.urlopen(link)
            print website.getcode()
            website.close()
        except:
            print link

print count1