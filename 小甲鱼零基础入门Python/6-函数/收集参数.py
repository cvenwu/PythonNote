



def test(* params):
    """
    收集参数其实就是不定参数, 这里是将参数进行收集打包成一个元祖传递给tuple类型的params
    :param params:
    :return:
    """
    print("有 %d 个参数" % len(params))
    print("第2个参数是: ", params[1])


test(1, 2, 3, 4, 5, 6)


# 收集参数后面还有参数的时候，在调用的时候就应该使用关键参数来指定
def test2(* params, extra):
    print("收集参数是 : ",  params)
    print("位置参数是 : ", extra)

test2(5, 99, 89, extra = 45)


# 向函数参数传递列表
def test3(* params):
    print("有 %d 个参数" % len(params))
    print("第2个参数是: ", params[1])

li = [1,2,3,4,5]
test3(li)   # 报错
test3(*li)  # *会对其进行解包


