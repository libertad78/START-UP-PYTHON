month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(month31)
print(week)
print(month31[1:4]) #2개 이상의 자료는 리스트 형태로 출력되나, 1개씩 꺼내면 고유의 자료형(문자, 숫자, 실수 등)의 속성을 가짐
print(week[1])
print(week[-5:-2]) #화요일부터 목요일까지 음수 리스팅



# 리스트 함수
empty = []

#append() 괄호 안 요소를 리스트 맨 뒤에 하나씩 추가해주는 함수
empty.append('list')
empty.append('13')
empty.append('python')
print(empty)


#empty = ['list', 13, 'python']
#insert(n, '') n 위치에 ''를 삽입 
empty.insert(1, 'life')
print(empty)
#empty = ['list', 'life', 13, 'python']

# pop() 안에 아무 것도 없을 때는 맨뒤에꺼 삭제
empty.pop() # list-life-13-python 중에 파이썬 삭제됨
print(empty)

#pop() 안에 인덱스가 있으면 인덱스 위치의 요소 삭제
empty.pop(0) #list-life-13 중에 list 삭제됨
print(empty)
#empty = ['life', 13]

# remove(요소) 삭제: 내가 원하는 값을 찾아서 삭제
week.remove('WED')
print(week)

#empty = ['life', 13]
# clear
empty.clear()
print(empty)



#변수이름.함수이름(요소 or 인덱스) 가 아니라
# sum(리스트이름): 리스트 안에 요소를 전부 더해라
plus = month30[0]+month30[1]+month30[2]+month30[3]
plus2 = sum(month30)
print(plus)
print(plus2)

#IndexError: list index out of range: 리스트 안에 6개까진데 8번째(없는 위치) 값을 가져오라고 할 때 발생하는 에러
print(len(week)) #몇개인지 셀 수 있음
#print(week) len으로 리스트를 셀 때는 글자수가 아니라 안에 있는 요소의 개수를 세주는 것


# + 활용 리스트 합치기

month = month30 + month31   #extend를 쓰지 않아도 + 를 사용하여 리스트끼리 합칠 수 있음
month_1 = month30 * 4  #곱하기 n만큼 반복해서 합쳐짐
print(month)
print(month_1)

# extend 리스트끼리 합병 (뒤에 이어붙여서 삽입)
month31.extend(month30)
print(month31)