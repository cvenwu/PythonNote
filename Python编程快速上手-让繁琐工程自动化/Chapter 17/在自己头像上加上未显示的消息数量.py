from PIL import Image, ImageDraw
import urllib.request

# 读取QQ头像
qq_number = input('请输入QQ号: ')
src = "http://q1.qlogo.cn/g?b=qq&nk=" + qq_number + "&s=100"
response = urllib.request.urlopen(src)
html = response.read()

# 将QQ头像写入文件icon.png
with open('icon.png', 'wb') as f:
    f.write(html)

# 利用PIL模块将头像上方添加未读消息数量
img = Image.open('icon.png')
print(img.size)
img2 = img.copy()
img3 = ImageDraw.Draw(img2).text((82, 0), '99+', 'red')
img2.save('icon2.png')

