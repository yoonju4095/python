# print() - 서식 출력
data = 123
print('입력하신 값은 %5d 입니다' % data)
print('%05d' % data)

data = 123.45
print('%f' % data)
print('%10.1f' % data)
print('%-10.3f' % data)

data = 'python'
print('%s' % data)
print('%10s' % data)