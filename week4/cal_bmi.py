# P.152 11번

def cal_bmi(height, weight):    # cal_bmi 함수 정의
    bmi = weight / (height * height)    # BMI = 체중(kg) / 키(m) * 키(m)
    print("당신의 BMI: ", bmi)

    if 20.0 <= bmi < 25.0:      # BMI 지수가 20~24.9면 정상
        print("정상입니다.")
    elif 25.0 <= bmi < 30.0:    # BMI 지수가 25~29.9면 과체중
        print("과체중입니다.")
    elif 30 <= bmi:             # BMI 지수가 30 이상이면 비만
        print("비만입니다.")

while True:
    weight = input("무게(kg): ")  # 사용자로부터 무게를 입력받는다.
    height = input("키(m): ")    # 사용자로부터 키를 입력받는다.
    cal_bmi(float(height), float(weight))