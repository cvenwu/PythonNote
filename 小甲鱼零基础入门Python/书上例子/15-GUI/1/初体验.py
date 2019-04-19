import tkinter as tk

# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title('KTV点歌界面')
# 添加一个Label组件，Label组件是GUI程序中最常用的组件之一，可以显示图标，图片以及文本
theLabel = tk.Label(root, text = "我的第二个窗口程序")
# 调用Label.pack()方法用于自动调节组件自身的尺寸
theLabel.pack()
# 注意，此时窗口不会显示，除非执行下面代码
root.mainloop()




