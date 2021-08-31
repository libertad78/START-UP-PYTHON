
# 재귀함수: 자기 자신을 호출하는 함수
# 팩토리얼: 5! = 5*4*3*2*1 = 120

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial_r(n):
    if n == 0:  # 탈출조건
        return 1
    else:
        return n * factorial_r(n-1)

n = int(input("숫자: "))        
print(factorial(n))
print(factorial_r(n))


# 피보나치 수열: 1 1 2 3 5 8 13 21 34 ...
# n번째 숫자는 n-1번째 숫자에다 n-2번째 숫자를 더한 수
# f(1)=1, f(2)=1, f(n)=f(n-1)+f(n-2)
# 4번째 숫자: [2번 = 4-2 반복해야 구할 수 있음]
# 5번째 숫자: [3번 = 5-2 반복해야 구할 수 있음]
# 6번째 숫자: [4번 = 6-2 반복해야 구할 수 있음]

def fibonacci(n):
    fibo = [1, 1]
    if n == 1:
        return fibo[0] # or return 1
    elif n == 2:
        return fibo[1] # or return 1
    else:
        for i in range(1, n-1):  # n = 3, range(1, 2)
            temp = fibo[i] + fibo[i-1]  # temp = fibo[1]+fibo[0] = 2
            fibo.append(temp) # fibo = [1, 1, 2]
        return fibo[n-1]  # fibo[2] = 2
    
print(fibonacci(n))



# 재귀함수(탈출조건)으로 더 짧게 코딩하기

def fibonacci_r(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)

print(fibonacci(n))
print(fibonacci_r(n))