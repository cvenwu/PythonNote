def c2f(cel):
    fah = cel * 1.8 + 32
    return fah


def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel


def test():
    print("测试,0摄氏度 = %.2f华氏度" % c2f(0))
    print("测试,0摄氏度 = %.2f华氏度" % f2c(0))


# 为什么要__name__ == '__main__' 是用来判断当前模块是单独运行还是导入到其他程序中，如果是单独运行将会执行if的语句块
if __name__ == '__main__':
    test()

