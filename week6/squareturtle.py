import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(lenght):         # lenght는 한변의 길이
    t.down()
    for i in range(4):
        t.forward(lenght)
        t.left(90)
    t.up()

square(100)                  # square() 함수를 호출한다.
t.forward(120)
square(100)
t.forward(120)
square(100)

turtle.mainloop()
turtle.bye()