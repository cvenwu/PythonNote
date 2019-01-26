# 对于输入的数大小进行相应的提示
guess = input('请输入一个整数：')
guess = int(guess)
if guess == 8:
    print("哇草，你是小甲鱼心里的蛔虫吗?")
    print("哼，猜中了也没有奖励")
else:
    if guess > 8:
        print("哥，大了大了~~~")
    else:
        if guess < 8:
            print("嘿，小了！小了！！")
print("游戏结束，不玩啦~~~~")





