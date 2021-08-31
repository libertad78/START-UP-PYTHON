
date = input("출력을 원하는 해와 달을 입력해주세요(해.월):").split('.')
day = input("첫째날은 몇 요일인가요?(MON/TUE/WED/THU/FRI/SAT/SUN): ")

#        0   1   2   3   4   5   6   7   8   9   10  11  
month = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2월처럼 변수가 있을 경우 다른 특별한 것으로 표시

#         0      1      2      3      4      5      6
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 형변환
for i in range(len(date)):
    date[i] = int(date[i])

y = date[0]  # 연도
m = date[1]  # 달




'''
if m>=1 and m<=12:
    if m == 2:
        if (y % 4 ==0 and y % 100 != 0) or (y % 400 == 0) : 
            # 윤년은 4로 나누어떨어지면서 100으로 나누어 떨어지지 않거나 400으로 나누어 떨어짐
            print(f"\t    {m}")    # \t는 공백을 의미. \ 1개가 8칸이므로 \t 뒤에 스페이스 4번하면 총 12칸 스페이스
            print("SUN MON TUE WED THU FRI SAT")
            temp = week.index(day) # index(XXX) XXX가 어떤 위치에 있는지 반환해주는 함수
            for i in range(temp):
                print("    ", end = "")
            for i in range(1, 30):  # 인덱스와 실제 월과의 차이 -1 range 미만이므로 +1
                print("{:3d}".format(i), end = " ")
                temp = temp + 1
                if temp % 7 == 0:
                    print()

        else: 
            print(f"\t    {m}")    # \t는 공백을 의미. \ 1개가 8칸이므로 \t 뒤에 스페이스 4번하면 총 12칸 스페이스
            print("SUN MON TUE WED THU FRI SAT")
            temp = week.index(day) # index(XXX) XXX가 어떤 위치에 있는지 반환해주는 함수
            for i in range(temp):
                print("    ", end = "")
            for i in range(1, 29): # 인덱스와 실제 월과의 차이 -1, range 미만이므로 +1
                print("{:3d}".format(i), end = " ")
                temp = temp + 1
                if temp % 7 == 0:
                    print()

    else:
        print(f"\t    {m}")    # \t는 공백을 의미. \ 1개가 8칸이므로 \t 뒤에 스페이스 4번하면 총 12칸 스페이스
        print("SUN MON TUE WED THU FRI SAT")
        temp = week.index(day) # index(XXX) XXX가 어떤 위치에 있는지 반환해주는 함수
        for i in range(temp):
            print("    ", end = "")
        for i in range(1, month[m-1]+1): # 인덱스와 실제 월과의 차이 -1, range 미만이므로 +1
            print("{:3d}".format(i), end = " ")
            temp = temp + 1
            if temp % 7 == 0:
                print()

else :
    print("잘못된 날짜입니다.")
'''


# 유지보수
if 1<=m and m<=12:
    if m == 2:
        if (y % 4 ==0 and y % 100 != 0) or (y % 400 == 0) : 
            month[1] = 29

        else: 
            month[1] = 28

        print(f"\t    {m}")    # \t는 공백을 의미. \ 1개가 8칸이므로 \t 뒤에 스페이스 4번하면 총 12칸 스페이스
        print("SUN MON TUE WED THU FRI SAT")
        temp = week.index(day) # index(XXX) XXX가 어떤 위치에 있는지 반환해주는 함수
        for i in range(temp):
            print("    ", end = "")
        for i in range(1, month[m-1]+1): # 인덱스와 실제 월과의 차이 -1, range 미만이므로 +1
            print("{:3d}".format(i), end = " ")
            temp = temp + 1
            if temp % 7 == 0:
                print()

else :
    print("잘못된 날짜입니다.")