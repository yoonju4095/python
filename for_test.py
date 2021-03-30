for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(1, 6, 2):    # 1, 3, 5
    print(i)

# 역순
for i in range(10, 0, -1):
    print(i, end="\n")

# 구구단 출력
for i in range(1, 10):
    for j in range(1,10):
        print(i, "*", j, "=", j*i)
    print('------------')

# 1부터 n까지의 합
sum = 0
n = 10
for i in range(1, n+1):
    sum = sum + i
print("합 =", sum)


n = int(input("정수를 입력하시오:"))
fact = 1
for i in range(n, 0, -1):
    fact = fact * i
print(fact)
print(n, "!은", fact, "이다.")
