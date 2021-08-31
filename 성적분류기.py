name = input("이름을 입력하세요 : ")
s1 = input("과목1을 입력하세요 : ")
s2 = input("과목2을 입력하세요 : ")
s3 = input("과목3을 입력하세요 : ")
management = int(input("경영 성적을 입력하세요 : "))
economy = int(input("경제 성적을 입력하세요 : "))
coding = int(input("코딩 성적을 입력하세요 : "))

#print(f'연봉은{salary_y}원 입니다.')
#print('연봉은{:7.2f}원 입니다.'.format(salary_y))
print("--------<성적표>--------")
print(f'이름 : {name}')


#해당주차 과제 답안 파일 + 4주차 수업자료 파일 앞부분에 있는 모범사례와 비교하기

if management > 90 and management <= 100 :
    print("경영 등급: A")
elif management > 80 and management <=90 :
    print("경영 등급: B")
else :
    print("경영 등급: C")


if economy > 90 and economy <= 100 :
    print("경제 등급: A")
elif economy > 80 and economy <=90 :
    print("경제 등급: B")
else :
    print("경제 등급: C")

if coding > 90 and coding <= 100 :
    print("코딩 등급: A")
elif coding > 80 and coding <=90 :
    print("코딩 등급: B")
else :
    print("코딩 등급: C")

