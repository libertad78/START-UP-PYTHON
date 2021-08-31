#부울 변수 연습
#비교연산자: >, <, ==, !=, >=, <=
# = 은 우변을 좌변에 넣어라 이기 때문에

print( 5 > 3 )
print( 5 < 3 )
print( 1 == 1 )
print(1 != 2 )
print(4 <= 8) #true
print(8 != 8) #false
#Terminal: True, False, True, True, True, False


#논리연산자: and, or, not(T>F, F>T 부호 변경 역할)
#조건문: if, elif, else(뭣도 아닐 때)

x = float(input("학점을 입력하세요 : "))


if x == 4.5 :
    print("신")
elif x >= 4.2 and x < 4.5 :
    print("교수님의 사랑")
#C 같은 언어는 elif if x >= 4.0 하면 오류뜸
elif x >= 3.5 and x < 4.2 :
    print("현 체제의 수호자")
else :
    print("분발해주세요~")