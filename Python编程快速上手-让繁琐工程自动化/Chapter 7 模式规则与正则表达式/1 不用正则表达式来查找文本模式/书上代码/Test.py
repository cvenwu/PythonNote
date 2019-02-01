from isPhoneNumber import *
print(isPhoneNumber('123'))
print(isPhoneNumber('145-555-1442'))

# 检查一段文本内容是否包含电话号码
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
