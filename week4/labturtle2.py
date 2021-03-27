# p.134 LAB 프로그램을 함수를 사용하여 수정

import turtle

t = turtle.Turtle() # 거북이를 만든다.
t.shape("turtle")   # 커서의 모양을 거북이로 한다.
t.width(3)  # 거북이가 그리는 선의 두꼐를 3배로 한다.
t.shapesize(3, 3)   # 거북이를 3배 확대한다.

# tur: turtle 객체
# rad: 반지름
# move: 이동거리
def turtleLeftMove(t, rad, move):     # turtleLeftMove 함수 정의
    t.circle(rad)
    t.forward(move)

def turtleRightMove(t, rad, move):   # turtleRightMove 함수 정의
    t.circle(rad)
    t.forward(move)


while True:
    command = input("명령을 입력하시오: ")  # 사용자로부터 명령을 입력받는다.
    if command == "l":  # 사용자가 "l"을 입력하였으면
        turtleLeftMove(t, 90, 100)

    if command == "r":  # 사용자가 "r"을 입력하였으면
        turtleRightMove(t, 90, 100)

    if command == "q":  # 사용자가 "q"을 입력하였으면
        break   # 무한 루프를 빠쟈나간다.

turtle.mainloop()
turtle.bye()