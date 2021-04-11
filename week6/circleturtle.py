import turtle

t = turtle.Turtle()  # 거북이를 생성한다.
t.shape("turtle")  # 커서의 모양을 거북이로 만든다.

radius = 50  # 원의 반지름 50으로 준다.
count = 3  # 개수를 3으로 준다.

def circleDraw(radius, count):  # circleDraw() 함수 정의

    for i in range(count):  # count 만큼 반복한다.
        t.up()  # 펜을 올려서 커서의 이동흔적이 표시 안되게 하기
        t.forward(radius * 2 + 20)  # 원의 지름 + 20 만큼 이동
        t.down()  # 펜을 내려서 커서의 이동흔적이 표시되게 하기
        t.circle(radius)  # 반지름이 radius인 원 그리기

    return turtle

circleDraw(radius, count)  # circleDraw() 함수 호출

turtle.mainloop()
turtle.bye()