

count = 10


def myFu():
    count = 5  # 这里将会创建一个局部变量，并不会修改全局变量的值
    print(count)
myFu()
print(count)



def myFun():
    global count   # 声明count 为全局变量，而不是局部变量
    count = 5
    print(count)

myFun()
print(count)
