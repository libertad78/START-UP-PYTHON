n = int(input("숫자를 입력하세요: "))

def divisor(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

print(f"{n}의 약수: {divisor(n)}")

if len(divisor(n)) == 2:
    print(f"숫자 {n}은 소수입니다")

else:
    if sum(divisor(n)) - n == n:
        print(f"숫자 {n}은 완전수입니다")
    else:
        print(f"숫자 {n}은 일반수입니다")

