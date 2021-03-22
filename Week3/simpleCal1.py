def add(a, b):
    return a + b


def substract(a, b):
    return a - b

while True:
    a = input("a : ")
    if a != 'q':
        op = input("+, - : ")
        b = input("b : ")
        if op == "+":
            res = add(int(a), int(b))
        elif op == "-":
            res = substract(int(a), int(b))
        else:
            print("input error")

        print("result : ", res)
        print("-------------------")
    else:
        print('good bye')
        exit(0)
