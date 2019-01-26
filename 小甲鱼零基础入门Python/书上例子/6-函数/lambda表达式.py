




def ds(x):
    return 2 * x + 1


print(ds(5))

print(lambda x: 2 * x + 1)  # 返回一个函数对象，如果要进行使用，只需要进行简单赋值就好

f = lambda x : 2 * x + 1
print(f(6))


# 带两个参数的lambda表达式
g = lambda x, y: x + y
print(g(3, 4))

