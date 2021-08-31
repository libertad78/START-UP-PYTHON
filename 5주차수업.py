
# input() 리스트 실습

name = "kim.ju.won"
name = name.split('.') # .을 기준으로 잘라줘
print(name)  # ['kim', ju', 'won'] 으로 출력됨

numbers = input().split() # input값을 띄어쓰기 단위로 split
print(numbers)

for i in range(len(numbers)): 
    numbers[i] = int(numbers[i])

print(numbers)

'''
# 튜플(tuple): 리스트는 [], 튜플은 ()
# 요소 삭제,생성,수정 불가 → 값을 변하지 않게 할 경우에만 활용

tup1 = () # 아무 것도 입력 안해도 선언 가능
tup1 = (1) # 하나의 자료에 접근하면 해당 자료만 나옴
tup2 = (1,2,3)
tup3 = ('apple', 'banana')
tup4 = 1, 2, 3, 4
tup5 = (('ab', 'cd'), 'ab', 'cd', True)

print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)

print(tup4[1:]) # 앞숫자 인덱싱(사람 기준 2번째)부터 뒤로 쭉
print(tup3[1])
print(tup3[-1])

#tup4[3] = 7 # tup4의 3번째 위치(컴퓨터 기준) 값을 7로 바꿔
numbers[3]= 8 # 컴퓨터 기준 3번째이므로 사람 기준 4번째 값이 8로 바뀜
print(numbers)

# + *
plus_tup = tup3 + tup2
multiple_tup = tup3 * 3

print(plus_tup)
print(multiple_tup)
'''
'''
# 딕셔너리: 키를 기반으로 저장하는 자료형 그룹 {}
# 변수이름 = { 키 : 값 }

dictionary_1 = { # 딕셔너리는 여러 값을 한 번에 보기 불편하므로 엔터키로 구분(pythonic)
    'apple' : '사과',
    'banana' : '바나나',
    'orange' : '오렌지',
    'watermelon' : '수박'
}

print(dictionary_1)
print(dictionary_1['apple']) # index를 숫자가 아니라 키로 넣은 것
#print(dictionary_1[9]) # 없는 인덱스라서 KeyError 빌셍



# 어떻게 dictionary를 for문, 조건문에서 활용하는지
if '이름' in dictionary_2:
    print(dictionary_2['이름'])

if '집주소' in dictionary_2:
    print(dictionary_2['이름'])  # 키(집주소)가 없어서 실행조차 안됨


# get 함수: 변수[키값]이랑 동일한 효과
print(dictionary_2.get('학과'))  # 키를 이용해서 해당 값을 찾는다
print(dictionary_2.get('파이썬')) # 파이썬은 키X 값O

dictionary_2 = {
    '이름' : '김주원',
    '나이' : '미상',
    '학과' : '컴퓨터전자시스템 공학부',
    '수업' : '파이썬'
}

keys = []  ##### 여기서부터 이해 못함...
value = []
for key in dictionary_2:  #key는 임시변수
    keys.append(key)  # 키값을 가져와서 추가
    print(dictionary_2[key]) # 다른 인덱스(숫자)는 n번째 해당하는 값이 append 되었지만 dictionary는 키값이 append됨
    value.append(dictionary_2[key]) # value를 가져와서 추가
print(value)
print(key)

# 키(키값)을 통해 판단한다 / 값은 value 라고 부른다
'''

'''
key_value = []
for key, value in dictionary_2:
    key_value.append(key, value)
print(key_value)
'''