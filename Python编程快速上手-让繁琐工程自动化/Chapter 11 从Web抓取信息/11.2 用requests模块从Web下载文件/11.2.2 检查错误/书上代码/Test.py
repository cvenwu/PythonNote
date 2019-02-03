"""
@description 检查错误
    方法一：看Request对象的status_code == Response对象的codes的ok
    方法二：调用Response对象的raise_for_status() ，如果下载出错，将会抛出异常，如果下载成功，什么也不会做
                              raise_for_status()是一种很好的方式，确保程序在下载失败时停止。
"""


import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(len(res.text))
if res.status_code == requests.codes.ok:    # 了解下载是否成功
    print(res.text[:250])

res.raise_for_status()     # 检查成功的第2种方法，调用Response对象的