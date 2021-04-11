# p.246 04번

def getGrade(score):      # getGrade 함수 정의, score는 매개변수
    if score >= 90:       # 성적이 90점 이상이면 A
        grade = "성적은 A 입니다."
    elif score >= 80:     # 성적이 80점 이상이면 B
        grade = "성적은 B 입니다."
    elif score >= 70:      # 성적이 70점 이상이면 C
        grade = "성적은 C 입니다."
    elif score >= 60:      # 성적이 60점 이상이면 D
        grade = "성적은 D 입니다."
    else:                  # 그외의 점수는 F
        grade = "성적은 F 입니다."
    return grade

score=int(input("점수를 입력하세요: "))    # 사용자로부터 점수를 입력받아서 score에 저장합니다.

print(getGrade(score))  # getGrade() 함수를 호출한다.



