import lotto

n = int(input("로또 길이: "))

l = lotto.lotto_generator(n)

while True:  # 제대로 된 로또를 입력했을 때까지 무한루프 걸기
    temp = input("복권을 뽑아주세요: ").split()
    if lotto.checker(n, temp) == True:
        break
    print("잘못된 복권입니다.")

for i in range(len(temp)):
    temp[i] = int(temp[i])

lotto.print_lotto(l)
lotto.win(l, temp)