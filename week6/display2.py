# 과제 01번

def display(msg="welcome", count=1):    # 매개변수 msg에 디폴트인수로 "welcome"을 준다.
    for k in range(count):  # count 만큼 반복한다.
        print(msg)  # msg 값을 출력한다.

display()   # 함수 display()를 호출하면 welcome이 한번 출력된다.