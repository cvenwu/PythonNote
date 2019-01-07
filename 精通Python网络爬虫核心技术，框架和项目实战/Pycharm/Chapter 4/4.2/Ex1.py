import urllib.request

file = urllib.request.urlopen("https://www.apple.com/cn/")
data = file.read()
dataLines = file.readlines()
dataLine = file.readline()
print(data)
print(dataLine)
print(dataLines)


# 将读取到的内容保存到本地
file = open("E:/爬取到的内容/apple_cn.html", "wb")
file.write(data)
file.close()


