"""
功能：通过输入命令行参数，给定参数，然后对天猫上的商品进行查找，然后只返回5个商品页面
"""

import sys
import bs4
import requests
import webbrowser
url = 'https://list.tmall.com/search_product.htm?q=' + sys.argv[1]
print(url)
resp = requests.get(url)
print(resp.text)
resultSoup = bs4.BeautifulSoup(resp.text)
print(resultSoup)
count = 0
for i in resultSoup.select('.productTitle a'):
    if count == 5:
        sys.exit()
    count += 1
    webbrowser.open(i.get('href'))
