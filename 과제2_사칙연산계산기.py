def plus(a,b):
    result = a + b
    return result

def minus(a,b):
    result = a - b
    return result

def multiple(a,b):
    result = a * b
    return result

def division(a,b):
    result = a / b
    return result

def share(a,b):
    result = a // b
    return result

def rest(a,b):
    result = a % b
    return result

n, m = input("두개의 숫자를 입력하세요: ").split()
n = int(n) # 형변환
m = int(m) # 형변환

what = input("연산자를 입력하세요: ")

if what == "+":
    print(plus(n,m))

elif what == "-":
    if n >= m:
        print(minus(n,m))
    else:
        print("첫번째 입력한 수가 두번째 입력한 수보다 작습니다! 다시 입력해주세요!")

elif what == "*":
    print(multiple(n,m))

elif what == "/":
    if m != 0:
        print('{:.2f}'.format(division(n,m)))
    else:
        print("0으로 나눌 수 없습니다! 다시 입력해주세요!")

elif what == "//":
    if m != 0:
        print(share(n,m))
    else:
        print("0으로 나눌 수 없습니다! 다시 입력해주세요!")

elif what == "%":
    if m != 0:
        print(rest(n,m))
    else:
        print("0으로 나눌 수 없습니다! 다시 입력해주세요!")

else:
    print("잘못된 값입니다! 다시 입력해주세요!")
