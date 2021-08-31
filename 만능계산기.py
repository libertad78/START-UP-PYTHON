print("계산기 매뉴얼은 다음과 같습니다")
print("1: 사칙연산계산기 2: 환율계산기 3: 연봉계산기")
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

else:
    print("올바른 매뉴얼을 입력해 주세요")

    