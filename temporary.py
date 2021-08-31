'''
import temporary   

n = input("국가: ")
m = int(input("원화: "))

temporary.currency(m, n)
'''

# 가위바위보
# 난수: 숫자를 마음대로 랜덤하게 생성하는 라이브러리

import random

# random(): 0~1 사이 소수를 무작위로 생성하는 함수
print(random.random())

# randrange(max) 
# randrange(이상, 미만)
print(random.randrange(100))
print(random.randrange(10, 1000))


print("<컴퓨터와 함께하는 가위바위보>")
list_a = ["가위", "바위", "보"]
computer = random.choice(list_a)

user = input("가위바위보: ")
print(f"사용자: {user} / 컴퓨터: {computer}")

if user == "가위" and computer == "가위":
    print("무승부입니다")
elif user == "가위" and computer == "바위":
    print("당신이 졌습니다!")
elif user == "가위" and computer == "보":
    print("당신이 이겼습니다.")
elif user == "바위" and computer == "가위":
    print("당신이 이겼습니다.")
elif user == "바위" and computer == "바위":
    print("무승부입니다")
elif user == "바위" and computer == "보":    
    print("당신이 졌습니다!")
elif user == "보" and computer == "가위":
    print("당신이 졌습니다!")
elif user == "보" and computer == "바위":
    print("당신이 이겼습니다.")
elif user == "보" and computer == "보":   
    print("무승부입니다")
else:
    print("가위 바위 보 중에서 입력해주세요~") 
