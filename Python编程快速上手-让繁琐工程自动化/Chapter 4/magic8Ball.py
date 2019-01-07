import random



def getAnswer(answerNumber):
    if answerNumber == 1:
        return '1'
    elif answerNumber == 2 :
        return '2'
    elif answerNumber == 3 :
        return '3'

randomNum = random.randint(1, 3)        #得到一个在1和3之间，包括1和3的随机整数

fortune = getAnswer(randomNum)

print(fortune)

