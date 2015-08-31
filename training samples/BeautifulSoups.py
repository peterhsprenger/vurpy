# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import urllib2
url1 = "http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/"
url2 = 'http://www.worldcat.org/oclc/846557519'
url3 = 'http://www.worldcat.org/title/erlebnisraum-lutherstadt-wittenberg-genese-entwicklung-und-bestand-eines-protestantischen-erinnerungsortes/oclc/846557519&referer=brief_results'
content1 = urllib2.urlopen(url1).read()
content2 = urllib2.urlopen(url2).read()
content3 = urllib2.urlopen(url3).read()
soup = BeautifulSoup(content3, 'lxml')


#print soup.prettify()
#print(soup.get_text())
#print soup.title.string
#print soup.p
#print soup.a
  
#for link in soup.find_all('a'):
#    print(link.get('href'))

#<li class="subject-term">
#<a href="/search?q=su%3AProtestantismus.&qt=hot_subject" lang='' title="Suche nach weiteren Themengebieten">Protestantismus.</a>

images = soup.find_all('img')
#for image in images: 
#   print image
#print images[0]['src']

#Content 2
topics2 = soup.find_all('li', {'class': 'subject-term'})
for topic in topics2:
    print topic.text


# Content 3    
# <a style="text-decoration:none" href="http://schema.org/about">schema:about</a> 
# <<a href="http://viaf.org/viaf/14773105" property="schema:about" resource="http://viaf.org/viaf/14773105">http://viaf.org/viaf/14773105</a>>
# <span style="color: orange"> # Martin Luther</span>
  
topics3 = soup.find_all('a', {'href': 'http://schema.org/about'})
for topic in topics3:
    print topic.findNext('span').text.replace('#', '')
    