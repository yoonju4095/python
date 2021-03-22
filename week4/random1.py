# 이 프로그램은 산수 문제를 출제한다.

import random

x = random.randint(1, 100)
y = random.randint(1, 100)

# f-String
# answer = int(input(f"{x} + {y} = "))

# format
answer = int(input('{0} + {1} = '.format(x, y)))


# 부울 변수에 결과를 저장하고 출력한다.
flag = (answer == (x+y))
print(flag)