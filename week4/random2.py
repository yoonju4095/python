# p.124 산술 문제 출제 프로그램

import random

x = random.randint(1, 100)  # 1부터 100사이의 난수를 불러와서 x에 저장한다.
y = random.randint(1, 100)  # 1부터 100사이의 난수를 불러와서 y에 저장한다.
score = 0   # 변수 score에 값을 저장한다.
count = 0   # 변수 count에 값을 저장한다.

while True:

    # f-String
    #answer = int(input(f"{x} + {y} = "))

    # format
    answer = int(input("{} + {} = ".format(x,y)))

    # 부울 변수에 결과를 저장하고 출력한다.
    flag = (answer == (x+y))
    print(flag)
    count += 1  # 문제 횟수 증가
    if flag == True:    # 문제를 맞추면 점수 10점 증가
       score += 10

    if count == 5:      # 5번(마지막) 수행 후 최종점수와 횟수를 출력한다.
        print('count =', count, 'score = ', score)
        break


