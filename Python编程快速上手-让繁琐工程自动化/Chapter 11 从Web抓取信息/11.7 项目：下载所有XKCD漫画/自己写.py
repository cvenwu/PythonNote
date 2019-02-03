import bs4
import requests

url = 'http://xkcd.com'
resp = requests.get(url)
respSoup = bs4.BeautifulSoup(resp.text)

# 下载当前页面的漫画
li = respSoup.select('#comic img')
print('ddd')
count = 0
for i in li:
    count += 1
    file = open(r'E:/Python下载的漫画' + str(count) + '.png', 'wb')
    imgFile = open(url + i.get('src'), 'rb')
    file.write(imgFile)

# 转入前一张漫画的链接

