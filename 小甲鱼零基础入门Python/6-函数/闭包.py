



def funX(x):
    """
    闭包：closure,
    :param x:
    :return:
    """
    def funY(y):
        return x * y
    return funY


print(funX(8)(5))
# i = funX(8)
# print(i(5))




def printNum():
    x = 5
    def add(y):
        nonlocal x
        x *= x
        return x
    return add(4)

print(printNum()())






