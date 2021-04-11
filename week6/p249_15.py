# p.249 15번

import turtle
t = turtle.Turtle() # 거북이를 만든다.
t.shape("turtle")   # 커서의 모양을 거북이로 만든다.

def draw_square(size):  #  draw_square() 함수 정의
    for i in range(4):
        t.fd(size)      # 거북이를 size 만큼 앞으로 이동
        t.left(90)      # 거북이를 90도 왼쪽으로 돌린다.
        size = size + 5 # size + 5

for i in range(10):     # 10번 반복한다.
    draw_square(i*20)   # i * 20

turtle.mainloop()
turtle.bye()    # turtlegraphics 창을 닫습니다.
