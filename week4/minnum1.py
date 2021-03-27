# P.150 05번

x, y, z = eval(input("3개의 정수를 입력하시오: "))    # 사용자로부터 3개의 정수를 입력받는다.

min = x     # min에 x 값을 넣는다.

if y < min: # min의 값이 y보다 크면 min에 y 값을 넣는다.
    min = y
if z < min: # min의 값이 z보다 크면 min에 z 값을 넣는다.
    min = z

print("제일 작은 정수는", min, "입니다.")  # 세 정수의 최소값 min을 출력한다.

