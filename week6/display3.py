# 과제 02번.

def display(msg, count=1, **kwargs):    # display() 함수를 가변인자로 작성하였다.
    for k in range(count):  # count 만큼 반복한다.
        print(msg)  # msg 값을 출력한다.
        print("kwargs = ", end=""), print(kwargs)   # end=" " 을 써서 줄바꿈 없이 한문장으로 출력한다.

display("welcome", a="welcome", b="welcome", c="welcome")  # 전달받은 키워드 인자를 Dictionary 형태로 저장한다.