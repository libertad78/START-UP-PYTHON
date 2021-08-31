nation = input("환전할 국가를 선택하세요: ")
won = int(input("원화를 입력하세요: "))

# 유럽, 영국, 중국, 일본, 미국 5가지로 if-elif-else
if nation == "유럽":
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
