# 이 프로그램은 산수 문제를 출제한다.

import random

x = random.randint(1, 100)  # 1부터 100사이의 난수를 불러와서 x에 저장한다.
y = random.randint(1, 100)  # 1부터 100사이의 난수를 불러와서 y에 저장한다.

# f-String
# answer = int(input(f"{x} + {y} = "))

# format
answer = int(input('{0} + {1} = '.format(x, y)))


# 부울 변수에 결과를 저장하고 출력한다.
flag = (answer == (x+y))
print(flag)