try:
    f = open('2.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件打开的过程中出错啦! 错误原因是 ' + str(reason))

