# p.150 03번

while True:
    command = input("문자를 입력하시오: ")      # 사용자로부터 하나의 문자를 입력받는다.
    if command == "R" or command == "r":    # 문자가 'R' 이나 'r' 이면 "Rectangle"이라고 출력한다.
        print("Rectangle")
    elif command == "T" or command == "t":  # 문자가 'T' 이나 't' 이면 "Triangle"이라고 출력한다.
        print("Triangle")
    elif command == "C" or command == "c":  # 문자가 'C' 이나 'c' 이면 "Circle"이라고 출력한다.
        print("Circle")
    else:
        print("Unknown")    # 그 외의 문자가 들어오면 "Unknown"이라고 출력하고 끝낸다.
        break