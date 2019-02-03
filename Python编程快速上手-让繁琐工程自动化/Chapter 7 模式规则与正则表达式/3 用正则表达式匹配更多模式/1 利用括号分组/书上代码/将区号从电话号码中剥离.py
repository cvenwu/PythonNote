import re
# 匹配字符串中将要剥离的利用括号进行分组，因为区号是前3位
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')


# group()参数传入0 或者 不传入参数将会输入匹配到的全部文本，传入1将会输出第1个分组, 使用groups()将会获得一个分组后的元祖
print(mo.group(0), mo.group(), mo.group(1), mo.group(2), mo.groups(), type(mo.groups()))
areaCode, mainNumber = mo.groups()





