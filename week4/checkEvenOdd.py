# p.126 홀수 짝수 판별 프로그램을 함수로 수정

def checkEvenOdd(n):    # checkEvenOdd 함수 정의
    if n % 2 == 0:      # 입력 받은 정수를 2로 나누었을 때 나머지가 0이면 짝수
        return "짝수"
    else:               # 0이 아니면 홀수
        return "홀수"

while True:
    number = int(input("정수를 입력하시오:"))   # 사용자로부터 하나의 정수를 입력받는다.
    if number == 0000:  # 값이 0000이면 끝낸다.
        print('bye bye')
        break
    else:

    # 함수 호출
     result = checkEvenOdd(number)

    # f-String
    print(f"결과값은 {result} 입니다")

    # format 함수
    # print('결과값은 {} 입니다'.format(result))