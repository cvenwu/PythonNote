# 采用循环，防止用户没有猜对的情况下多次运行程序
guess = input('请输入一个整数：')
guess = int(guess)
while guess != 8:
        if guess > 8:
            print("哥，大了大了~~~")
        if guess < 8:
            print("嘿，小了！小了！！")
        guess = input('请重新输入一个整数：')
        guess = int(guess)
else:
    print("哇草，你是小甲鱼心里的蛔虫吗?")
    print("哼，猜中了也没有奖励")
    print("游戏结束，不玩啦~~~~")
