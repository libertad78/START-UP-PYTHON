# 환전함수

def currency(won, nation):   # 정의일뿐. 호출해주어야 실행됨
    if nation == '유럽':
        euro = won / 1360
        print("{:8d}원은{:10.2f}유로입니다".format(won, euro))
    elif nation =='영국':
        pound = won / 1576
        print("{:8d}원은{:10.2f}파운드입니다".format(won, pound))
    elif nation =='중국':
        yuan = won / 177
        print("{:8d}원은{:10.2f}위안입니다".format(won, yuan))
    elif nation =='일본':
        yen = won / 10
        print("{:8d}원은{:10.2f}엔입니다".format(won, yen))
    elif nation =='미국':
        dollar = won / 1153
        print("{:8d}원은{:10.2f}달러입니다".format(won, dollar))
    else:
        print("국가에대한 정보가 없습니다.")


nation = input("환전할 국가를 선택하세요: ")
won = int(input("원화를 입력하세요: "))

currency(won, nation)



