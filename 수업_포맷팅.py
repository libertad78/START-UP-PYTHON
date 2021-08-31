# 연봉 계산기 과제
# 연봉을 입력 받음
salary_y =int(input("연봉을 입력하세요: "))

# 월급 계산
salary_m = salary_y /12
salary_w = salary_m / 4

# 출력
#print(f'연봉은{salary_y}원 입니다.')
#print(f'월급은{salary_m}원 입니다.')
#print(f'주급은{salary_w}원 입니다.')



# format 함수
print('연봉은{:10.2f}원 입니다.'.format(salary_y))
print('월급은{:10.2f}원 입니다.'.format(salary_m))
print('주급은{:10.2f}원 입니다.'.format(salary_w))
#2는 소수점 개수, 10은 소수점 포함 열 자리까지 숫자가 들어가지 않더라도 자리를 비워두는 것, 남는 자리는 공백처리
#10자리보다 넘는 수를 입력하면? 그 이상의 수를 포맷팅하기보다 정확한 값을 표시하는 데 집중

print('연봉은{:7.2f}원 입니다.'.format(salary_y))
print('월급은{:7.2f}원 입니다.'.format(salary_m))
print('주급은{:7.2f}원 입니다.'.format(salary_w))
#백만 입력시 연봉은 포맷팅 자리수를 넘겨버려서 소수점부터 출력, 월급과 주급은 7자리 딱 맞아서 정렬된 것

#소수점만 제한: {.2f} >>> 정렬은 없고 소수점만 2자리까지 표시

#정수형
#print('연봉은{:10.0f}원 입니다.'.format(salary_y))
#print('월급은{:10.0f}원 입니다.'.format(salary_m))
#print('주급은{:10.0f}원 입니다.'.format(salary_w))



#word = '{}{}'.format (10, 20)
#print(word)
#word = '{} {}'.format (10, 20)
#print(word)
#word = '{}{}{}'.format (10, 20, 30)
#print(word)
#word = '{}{}{}'.format (10, 20)
#print(word)
#word = '{} {}'.format (20)
#print(word)