import requests
import bs4
import os

url = 'https://xkcd.com/'

while not url.endswith('#'):
    res = requests.get(url)
    print('Download the page %s ' % url)
    resSoup = bs4.BeautifulSoup(res.text)
    imageList = resSoup.select('#comic img')
    # TODO: Save the image file to E:/Python下载的漫画/
    for image in imageList:
        url = image.get('src')
        print('Download the image %s ' % url)
        res = requests.get('http:' + url)
        file = open(os.path.join('E:/Python下载的漫画/', os.path.basename(url)), 'wb')
        for content in res.iter_content(100000):
            file.write(content)
        file.close()

    # TODO: Go to previous page
    prevLink = resSoup.select('a[rel="prev"]')[0].get('href')
    url = 'http://xkcd.com' + prevLink
print('Done...')

