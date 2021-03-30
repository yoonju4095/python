import turtle
import random

t = turtle.Turtle()
t.shape('turtle')

while True:
    r = random.randint(1, 100)
    m = random.randint(1, 200)
    print("r = ", r, "m = ", m)

    t.right(r)
    t.forward(m)


turtle.mainloop()