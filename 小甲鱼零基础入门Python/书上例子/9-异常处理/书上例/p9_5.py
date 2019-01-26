
# 对多个异常统一处理
try:
    int('abc')
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()
except (OSError, TypeError) as reason:
    print('出错啦！ 错误原因是' + str(reason))

