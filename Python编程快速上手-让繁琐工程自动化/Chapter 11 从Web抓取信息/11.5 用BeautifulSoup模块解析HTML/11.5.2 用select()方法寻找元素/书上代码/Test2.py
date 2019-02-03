import bs4
exampleFile = open('../../example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
'''
    查找HTML 中标签为p的内容，并且返回
'''
for text in exampleSoup.select('p'):
    print(text.getText())

