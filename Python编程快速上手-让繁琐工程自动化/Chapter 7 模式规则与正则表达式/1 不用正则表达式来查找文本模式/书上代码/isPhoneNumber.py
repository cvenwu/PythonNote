

def isPhoneNumber(text):
    '''
    对于输入的文本不用正则表达式匹配来验证是否为电话号码，而使用规则来验证
        规则：长度为12位，3个数字，1个短横线，3个数字，1个短横线，再是4个数字
    :param text:    输入的文本，
    :return:
    '''
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True




