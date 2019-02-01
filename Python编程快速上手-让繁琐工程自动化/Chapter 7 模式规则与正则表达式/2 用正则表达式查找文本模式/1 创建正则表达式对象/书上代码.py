
import re
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # 传入一个字符串值，表示正则表达式，将返回一个Regex对象
print(type(phoneNumberRegex))

mo = phoneNumberRegex.search('My number is 415-555-4242 415-555-4848')  # 查找到会返回一个Match对象，否则返回None
print(type(mo.group())) # Match对象的gropu方法 返回北查找字符串中实际匹配的文本
print(mo.group())

