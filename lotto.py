import random

def lotto_generator(n):
    result = []
    for i in range(n):
        result.append(random.randrange(1, 11))
    return result

def checker(n, ticket):
    if len(ticket) == n:
        return True
    else:
        return False

def win(ticket, lotto_g):
    count = 0
    for i in range(len(ticket)): 
        if ticket[i] == lotto_g[i]:
            count = count + 1

    if count >= 3:
        print(f"복권 당첨 숫자가 {count}개 이상입니다! 1등입니다! 축하합니다~")
    elif count == 2:
        print(f"복권 당첨 숫자가 {count}개 입니다! 2등입니다! 축하합니다~")
    elif count == 1:
        print(f"복권 당첨 숫자가 {count}개 입니다! 3등입니다! 축하합니다~")
    else:
        print("꽝입니다!")
    
def print_lotto(ticket):
    print("복권:", end = " ")
    for i in ticket:
        print(i, end = " ")
    print()