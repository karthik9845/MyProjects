import requests, sys, webbrowser, bs4

print 'Googling.....'
payload={'q':' '.join(sys.argv[1:])}
#res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res=requests.get('http://google.com/search',params=payload)
#print(res.url)
#print res.headers
res.raise_for_status()
googleSoup=bs4.BeautifulSoup(res.text,"lxml")

links=googleSoup.select('.r a')
#print type(links)
for i in links:
	print i.getText().encode('ascii','ignore')
print 'Opening links....'
for link in links:
	webbrowser.open('http://google.com'+link.get('href'))