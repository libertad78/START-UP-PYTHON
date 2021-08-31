# 성적 분류기 만들기
name = input("이름을 입력하세요 : ")

#과목수
num = int(input("과목수를 입력하세요 : ")) # ex) 3

sub = []
score = []
grade = []

for i in range(num): #5개의 변수를 일일이 받아줄 필요X  # in range(3)=[0,1,2]
    temp = input(f'과목{i+1}을 입력하세요 : ') # 과목1, 과목2, 과목3을 입력하세요
    sub.append(temp) # sub 리스트에 입력 받은 과목 1~3 추가
#print(sub) # sub = ['국어', '영어', '수학']

for i in range(num): #5개의 변수를 일일이 받아줄 필요X
    temp = int(input(f"{sub[i]} 성적을 입력하세요 : "))  # 리스트 내의 index가 나타내는 값을 가져오는 것이므로 i+1이 아니라 i
    score.append(temp)
#print(score)

#아래와 같이 코드가 비경제적이었으나 위처럼 바뀜
# score_1 = int(input(f"{sub_1} 성적을 입력하세요 : ""))
# score_2 = int(input(f"{sub_2} 성적을 입력하세요 : ""))
# score_3 = int(input(f"{sub_3} 성적을 입력하세요 : ""))
   
for i in range(num):
    if score[i] >= 90 and score[i] < 100 : # 리스트 내의 index가 나타내는 값을 가져오는 것이므로 i+1이 아니라 i
        grade.append('A')
    elif score[i] >= 80 and score[i] < 90 :
        grade.append('B')
    elif score[i] >= 0 and score[i] < 80 :
        grade.append('C')
    else:
        print("잘못된 숫자를 입력하셨습니다.")

print("--------<성적표>--------")
print(f"이름: {name.upper()}")
for i in range(num):
    print(f"{sub[i]} 등급: {grade[i]}")