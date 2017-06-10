import requests,os,bs4

#We use beautiful soup to parse and requests module to retrieve pages

url='http://xkcd.com'
if not os.path.isdir('xkcd'):
    os.makedirs('xkcd')

while not url.endswith('#'):
	#Download the page
	print 'Downloading page %s...' % url
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	comicElem=soup.select('#comic img')
	if comicElem==[]:
		print 'Could not find comic image.'
	else:
		comicUrl=comicElem[0].get('src')
		#Download the image.
		print 'Downloading image %s...'% (comicUrl)
		res=requests.get(url+comicUrl)
		res.raise_for_status()
		#save the image to ./xkcd.
		imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	#Get th prev button url.
	prevLink=soup.select('a[rel="prev"]')[0]
	url='http://xkcd.com'+prevLink.get('href')

print 'Done'
