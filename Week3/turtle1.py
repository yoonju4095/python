import turtle

t = turtle.Turtle()
t.screen.setup(width=400, height=300)

t.penup()
t.goto(-100, -50)
t.pendown()

radius = 50
t.color("red")
t.circle(radius)

t.color("blue")
t.forward(30)
t.circle(radius)

t.color("green")
t.forward(30)
t.circle(radius)

turtle.mainloop()
turtle.bye()

