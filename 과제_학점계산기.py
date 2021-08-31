name = input("이름을 입력하세요 : ")
num = int(input("입력할 과목의 갯수를 입력하세요 : "))

sub = []
score = []
grade = []

for i in range(num): 
    temp = input(f"과목{i+1}을 입력하세요 : ")
    temp1 = input(f"{temp}의 성적을 입력하세요 : ")
    temp2 = input(f"{temp}의 학점을 입력하세요 : ")
    sub.append(temp)
    score.append(temp1)
    grade.append(temp2)

print("--------<성적표>--------")
print(f"이름: {name.upper()}")

for i in range(num):
    print(f"{sub[i]} 평점: {score[i]}")

    
if temp1 == "A+":
    sum = 4.5 * temp2

elif temp1 == "A":
    sum = 4 * temp2

elif temp1 == "B+":
    sum = 3.5 * temp2

elif temp1 == "B":
    sum = 3 * temp2

elif temp1 == "C+":
    sum = 2.5 * temp2

elif temp1 == "C": 
    sum = 2 * temp2

elif temp1 == "D+":
    sum = 1.5 * temp2

elif temp1 == "D":
    sum = 1 * temp2

elif temp1 == "F":
    sum = 0

else :
    print("잘못된 학점입니다")