from PIL import ImageColor, Image

# 得到红色的RGBA值
print(ImageColor.getcolor('red', 'RGBA'))


# 打开图片
img = Image.open('1.png')
print(type(img))


# 输出图片的基本信息
print(img.format)
print(img.size)         # 得到一个元祖,包含该图像的宽度和高度的像素数
print(img.filename)
print(img.format_description)


# 新建一张图片并保存
img2 = Image.new('RGBA', (200,200), 'blue')
img2.save('2.png')


# 裁剪图片
img3 = img.crop((200, 800, 500, 1080))
img3.save('3.png')


# 复制图片
img4 = img3.copy()


# 粘贴图片
img4.paste(img3, (20, 20))
img4.save('4.png')



