"""
@description 下载文件必须用 "写二进制" 模式打开该文件，即向函数传入字符串'wb',作为open()的第二个参数，即使该页面是纯文本的，
        例如前面下载的罗密欧与朱丽叶的文本，你也需要写入二进制的数据，而不是文本数据，目的是为了保存该文本中的"Unicode编码"
"""
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

playFile = open('RomeAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    """
    iter_content()方法在每次循环的迭代中，返回一段内容，每一段都是bytes数据类型，我们需要指定一段包含多少字节，10万字节通常是
    不错的选择，
    
    for 循环和 iter_content()的部分可能看起来比较复杂，但这是为了确保 requests 模块即使在下载巨大的文件时也不会消耗太多内存
    """
    playFile.write(chunk)
playFile.close()

