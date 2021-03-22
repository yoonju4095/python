def plus(a, b): #더하기 함수 생성
    return a + b


def minus(a, b): #뺴기 함수 생성
    return a - b


def multi(a, b): # 곱하기 함수 생성
    return a * b


def divi(a, b): # 나누기 함수 생성
    return a // b


while True:

    print(" 종료 하려면 : 0 ")
    number1 = int(input(" 첫번째 수 : "))  # 첫번째 수 입력 받기
    if number1 == 0:
        print(" 프로그램 종료 ")
        break
    oper = str(input(" +, -, *, / : "))  # 사칙연산 입력 받기
    number2 = int(input(" 두번째 수 : "))  # 두번째 수 입력 받기

    if oper == "+":     # + 면 plus 함수 호출
        res = plus(number1, number2)

    elif oper == "-":   # - 를 입력 받으면 minus 함수 호출
        res = minus(number1, number2)

    elif oper == "*":   # * 를 입력 받으면 multi 함수 호출
        res = multi(number1, number2)

    elif oper == "/":   # / 를 입력 받으면 divi 함수 호출
        res = divi(number1, number2)

    else:
        print('{} 연산자 없음'.format(oper))

    print(' 결과 : {} {} {} = {}'.format(number1, oper, number2, res))