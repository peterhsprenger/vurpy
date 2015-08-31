# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import urllib2



testurl1 = 'http://www.worldcat.org/oclc/846557519'
testurl2 = 'http://www.worldcat.org/title/erlebnisraum-lutherstadt-wittenberg-genese-entwicklung-und-bestand-eines-protestantischen-erinnerungsortes/oclc/846557519&referer=brief_results'

content2 = urllib2.urlopen(testurl1).read()
content3 = urllib2.urlopen(testurl2).read()

soup2 = BeautifulSoup(content2, 'lxml')
soup3 = BeautifulSoup(content3, 'lxml')

#SELECT SOUP-VARIABLE:
soup = soup3

#Cover-Links auslesen
cover = soup.find_all('img', {'class': 'cover'})
print cover[0]['src']

#Content 2
#topics2 = soup.find_all('li', {'class': 'subject-term'})
#for topic in topics2:
#    print topic.text


# Content 3    
# <a style="text-decoration:none" href="http://schema.org/about">schema:about</a> 
# <<a href="http://viaf.org/viaf/14773105" property="schema:about" resource="http://viaf.org/viaf/14773105">http://viaf.org/viaf/14773105</a>>
# <span style="color: orange"> # Martin Luther</span>
  
topics3 = soup.find_all('a', {'href': 'http://schema.org/about'})
for topic in topics3:
    print topic.findNext('span').text.replace('#', '')
