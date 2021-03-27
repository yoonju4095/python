import turtle

def turtleLeftMove(t, r, m, c):
     t.color(c)
     t.left(r)
     t.forward(m)

def turtleRightMove(t, r, m, c):
     t.color(c)
     t.right(r)
     t.forward(m)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3, 3)   # 거북이를 3배 확대한다.


while True:
    command = input("명령을 입력하시오: ")
    radius = int(input("반지름: "))
    move = int(input("이동거리: "))
    col = input("색깔: ")
    if command == "l":  # 사용자가 "l"을 입력하였으면
        turtleLeftMove(t, radius, move, col)

    if command == "r":  # 사용자가 "r"을 입력하였으면
        turtleRightMove(t, radius, move, col)

    if command == "q":  # 사용자가 "q"을 입력하였으면
        break   # 무한 루프를 빠쟈나간다.

turtle.mainloop()
turtle.bye()