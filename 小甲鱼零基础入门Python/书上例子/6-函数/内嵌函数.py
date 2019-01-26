




def fun1():
    print("fun1()正在被调用......")
    def fun2():
        print("fun2()正在被调用.....")
    fun2()


fun1()

fun2()  # name 'fun2' is not defined


