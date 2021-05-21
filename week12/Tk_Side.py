# from tkinter import Tk, Label, RIGHT, LEFT, TOP, BOTTOM
# import tkinter
from tkinter import * # tkinter 모듈을 포함

window = Tk() # 루트 윈도우를 생성
print(type(window))

window.geometry("100x100") # height x width


label01 = Label(window, text="1.검색") # 레이블 위젯을 생성
label01.pack(side = RIGHT) # 레이블 위젯을 윈도우에 배체

label02 = Label(window, text="2.추가")
label02.pack(side = LEFT)

label02 = Label(window, text="3.삭제")
label02.pack(side = TOP)

label02 = Label(window, text="4.종료")
label02.pack(side = BOTTOM)


window.mainloop() # 윈도우가 사용자 동작을 대기