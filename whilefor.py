# 1 ~ 10 더하기
'''
count = 1
result = 0

while count <= 10 :
    result = result + count
    print("결과값: ", result)
    count = count + 1
    print("count 값: ", count)
    print("-------")  # 맨 아래까지 조건을 실행했다가 다시 올라가서 조건에 맞는지 확인함

print(f"합계 {result}")
'''


'''
# 만능계산기 whilefor로 유지보수 하기
while True : #무한루프문. 특정 조건에서 끝날 수 있도록 해야
    print("계산기 매뉴얼은 다음과 같습니다")
    print("1: 사칙연산계산기 2: 환율계산기 3: 연봉계산기 4: 종료 ")
    m_calculator = int(input("매뉴얼을 입력하세요: "))

    if m_calculator == 1: #사칙연산계산기

        manual = input("계산할 연산기호를 입력하세요: ")
        num_1 =int(input("첫 번째 정수를 입력하세요(두자리수 이하): "))
        num_2 =int(input("두 번째 정수를 입력하세요(두자리수 이하): "))

        if num_1 < 100 and num_2 < 100 :
            if manual == '+':
                add_result = num_1 + num_2
                print("덧셈결과: ", add_result)
            elif manual == '-': 
                if num_1 >= num_2 :
                    minus_result = num_1 - num_2
                    print("뺄셈결과: ", minus_result)
                else :
                    print("숫자가 잘못 되었습니다.")
            elif manual == '*':
                mul_result = num_1 * num_2
                print("곱셈결과: ", mul_result)
            elif manual == '//':
                if num_2 != 0 :
                    division_result_i = num_1 // num_2
                    print("정수 나눗셈 몫: ", division_result_i)
                else :
                    print("0으로 나눌 수 없습니다.")
            elif manual == '/':
                if num_2 != 0 :
                    division_result_f = num_1 / num_2
                    print("실수 나눗셈 결과: {:.1f}".format(division_result_f))
                else :
                    print("0으로 나눌 수 없습니다.")
            elif manual == '%':   
                if num_2 != 0 :
                    remain_result = num_1 % num_2
                    print("정수 나머지 결과: ", remain_result)
                else :
                    print("0으로 나눌 수 없습니다.")
            else :
                print("올바른 연산이 아닙니다.")
        else :
            print("두 자리 수가 아닙니다.")    

    elif m_calculator == 2: #환율계산기

        nation = input("환전할 국가를 선택하세요: ")
        won = int(input("원화를 입력하세요: "))

        if nation == "유럽" :
            euro = won / 1360
            print("{}원은 {:10.2f}유로 입니다".format(won, euro))
        elif nation == "영국":
            pound = won /1576
            print("{}원은 {:10.2f}파운드 입니다".format(won, pound))
        elif nation == "중국":
            yuan = won / 177
            print("{}원은 {:10.2f}위안 입니다".format(won, yuan))
        elif nation == "일본":
            yen = won / 10
            print("{}원은 {:10.2f}엔 입니다".format(won, yen))
        elif nation == "미국":
            dollar = won / 1153
            print("{}원은 {:10.2f}달러 입니다".format(won, dollar))
        else:
            print("해당되는 국가가 없습니다")


    elif m_calculator == 3: #연봉계산기

        salary_y =int(input("연봉을 입력하세요: "))
        salary_m = salary_y /12
        salary_w = salary_m / 4

        print('연봉은{:10.3f}원 입니다.'.format(salary_y))
        print('월급은{:10.3f}원 입니다.'.format(salary_m))
        print('주급은{:10.3f}원 입니다.'.format(salary_w))

    elif m_calculator == 4 :
        break #프로그램 종료


    else:
        print("올바른 매뉴얼을 입력해 주세요")
'''




# for루프문(리스트, range)
# i는 임시변수(이름은 상관없음). i가 리스트에 들어가서 하나씩 값을 가져옴

name = [1,2,3,4] 

for xlie in name : #임시변수는 리스트 안의 값을 가져와서 연산에 활용할 뿐
    xlie = xlie + 1
    print(xlie)
print(name) # 리스트 내의 값 자체를 변화시키지는 X

# 리스트 내의 값을 변화시키기 위해서는 range 사용
# range(n): 0이상 n미만 숫자 범위 지정해주는 객체
# range(n,m): n이상 m미만
# range(7): 0,1,2,3,4,5,6
# range(4,8): 4,5,6,7

for i in range(len(name)) : # for i in range(4) 랑 동일 → [0,1,2,3]
    name[i] = name[i] + 1 # [2,3,4,5]
    print(name[i])

print(name)

print("엔터를 하고 싶지 않아!", end = "") #''도 가능
print("확인!") #이 두 줄을 합치는 방법
# end = "." 이면 마지막에 마침표, "    " 이면 마지막에 띄어쓰기

