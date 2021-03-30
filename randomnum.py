# 숫자 맞추기 게임

import random

count = 0
num = 0
answer = random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while num != answer:
    num = int(input("숫자를 입력하시오:"))
    count = count + 1
    if num < answer:
        print("너무 낮음!")
    elif num > answer:
        print("너무 높음!")

if num == answer:
    print("정답입니다! 시도횟수 =", count)
else:
    print("정답은", answer)
