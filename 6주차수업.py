# 튜플, 리스트, 딕셔너리 비교
'''
#리스트: 여러 자료형 저장 가능, 인덱스로 접근 가능, 수정/삭제/추가가 자유로움, 다양한 함수 사용 가능
numbers = [1,2,3,4,5,6,7,8,9]

#튜플: 리스트와 비슷하나, 수정/삭제/추가 불가
tuple_1 = ('a', 'b', ('ab', 'cd'))

#딕셔너리: 키를 기반으로 저장하는 그룹형 자료형
dictionary_1 = {
    'apple' : '사과'
    'banana' : '바나나'
}

# 셋의 공통점
1) 서로 형변환 가능  ex) 리스트 자료 -> 튜플 자료
2) 반복문에 쓰일 수 있음
3) 여러가지 자료형을 요소로 가질 수 있음
(리스트, 튜플, 딕셔너리, 정수, 실수, 부울 변수, 문자열 등)
'''

# 형변환: 자료형(변수) 
# tuple, list, float, break, int는 변수명으로 하면 X

list_a = [1,2,3,4,5,6,7,8,8,8,9,9,9]
tuple_a = 3,5,7,9
dictionary_a = {
    '학생':'정태두',
    '보조강사':'김시은',
    '강사':'김시은'
}

list_b = tuple(list_a)
print(list_a)
print(list_b)

list_c = list(tuple_a)
print(list_c)
print(tuple_a)

list_d = list(dictionary_a)
print(list_d)  # value값을 모두 잃어버리고 key값으로 형변환됨(자료의 손실 발생)
print(dictionary_a)


# 리스트/튜플 VS 딕셔너리
# 리스트, 튜플은 인덱스가 0, 1, 2, ... / 역순 -1, -2, -3
# 딕셔너리는 인덱스가 아닌 키값을 통해 value 저장
# 튜플은 함수 사용 불가 / 리스트는 엄청 많은 함수 사용 가능
# 딕셔너리는 get(key), items(), values(), keys() 주로 사용
# get(key): key에 해당하는 value값 반환
# items(): key:value 반환
# values(): value값 반환 / keys(): key값 반환


# 집합: 중복 제거, 교/차집합 구해줌, -연산으로 차집합 구함
set_a = set(list_a)
print(set_a)
print(list_a)

name_a = set("Hello HUFS! Welcome!")
print(name_a)

# print(set_a[0]) # 에러 발생: 집합(set)에는 순서가 없기 때문에 인덱싱 불가
# list_e = list(set_a) 이런식으로 형변환하면 인덱싱 가능

set_b = set([1,2,3,4,5])
set_c = set([3,4,5,6,7])

# 연산자 사용
print(set_b - set_c) # 차집합(1,2) / (6,7)
print(set_b & set_c) # 교집합(3,4,5)
print(set_b | set_c) # 합집합(1,2,3,4,5,6,7)

# 함수 사용
print(set_b.difference(set_c)) # 차집합
print(set_b.intersection(set_c)) # 교집합
print(set_b.union(set_c)) # 합집합


# for 루프와 iterable (in 키워드)
# for루프는 iterable(반복가능한 자료형-순서 존재) 상에서만 활용 가능
# 순서 존재: range(), list, dictionary, tuple 등



'''
함수: 코드의 집합. 변수를 입력받아 사용자가 원하는 반환값을 돌려주는 역할
def: 함수 키워드. 컴퓨터에게 함수의 시작을 알림
함수이름(원형): def 키워드를 이용해 선언된 코드 부분. 함수의 매개변수, 반환값, 수행문 등을 정의
매개변수: 함수 호출 시 ()안에 넣어주는 함수의 여러가지 자료
리턴값(반환값): 함수를 호출해서 최종적으로 나오는 결과

코드의 의미있는 부분을 하나의 코드 꾸러미로 모아주므로,
다양한 출력 값을 가진 코드로 재사용 가능
무의미한 코드 반복을 줄여주고 유지보수에 효과적으로 사용됨
'''

# def 함수이름(매개변수1, 매개변수2):
#    수식
#    반환형


# 반환형이 있는 함수
def plus(a,b):
    result = a + b
    return result

n, m = input().split()
n = int(n) # 형변환
m = int(m) # 형변환
num = plus(n, m) #호출
print(num)
print(plus(n,m))


'''
# 반환형이 없는 함수
def plus(a,b):
    print(a+b)

n, m = input().split()
n = int(n)
m = int(m)
plus(n, m)
'''


# 함수를 통해 파일 불러오기

# 짝수 찾기
# 주어진 두 수 사이에 있는 짝수의 갯수(이상, 미만)

def even(num1, num2):
    count = 0
    for i in range(num1, num2):
        if i % 2 == 0:
            count = count + 1
    return count

n, m = input().split()
n = int(n)
m = int(m)
print(even(n, m))