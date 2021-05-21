# 엔트리 위젯
from tkinter import *
window = Tk()

entry01 = Entry(window, fg="black", bg="yellow", width=40)
entry01.pack(side=LEFT)

entry02 = Entry(window, fg="black", bg="green", width=40)
entry02.pack(side=RIGHT)

window.mainloop()