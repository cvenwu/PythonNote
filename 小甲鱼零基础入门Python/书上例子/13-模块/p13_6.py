import p13_5 as tc


print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99摄氏度 = %.2f华氏度" % tc.f2c(99))


print(__name__)     # 如果当前程序作为程序运行返回__main__否则返回模块名字
print(tc.__name__)