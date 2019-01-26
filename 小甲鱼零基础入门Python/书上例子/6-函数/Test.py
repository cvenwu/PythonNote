

def add(num1, num2):
    print(type(num1), type(num2))
    print(num1 + num2)


# add(1, 2)


def add1(num1, num2):
    # 下面三个引号中的内容是函数文档字符串，是不会被打印出来的，作为函数的一部分存储起来，可以通过函数名.__doc__获取
    """
    计算num1 与 num2的和
    :param num1: 用户传入的第一个数
    :param num2: 用户传入的第二个数
    :return:    两个数的和
    """
    return num1 + num2


print(add1(4, 5))

print(add1.__doc__)


def saySomething(name = 'yirufeng', words = 'sivan'):
    print(name + '->' + words)

saySomething(words='a', name='b')



