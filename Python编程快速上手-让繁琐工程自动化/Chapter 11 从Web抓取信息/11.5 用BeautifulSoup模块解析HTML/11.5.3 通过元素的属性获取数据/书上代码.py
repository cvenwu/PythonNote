import bs4
exampleSoup = bs4.BeautifulSoup(open('../example.html'))
spanElem = exampleSoup.select('span')[0]
print(type(spanElem))
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.attrs)

