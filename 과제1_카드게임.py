Jay = set(input("Jay가 선택한 카드(1~10에서 5장): ").split()) #리스트
Emily = set(input("Emily가 선택한 카드(1~10에서 5장): ").split())
Machine = set(input("기계가 선택한 카드(1~10에서 3장): ").split())


if len(Jay - Machine) > len(Emily - Machine):
    print(f"Jay대 Emily는 {len(Jay - Machine)}:{len(Emily - Machine)}로 Jay 승!")

elif len(Jay - Machine) < len(Emily - Machine):
    print(f"Emily대 Jay는 {len(Emily - Machine)}:{len(Jay - Machine)}로 Emily 승!")

elif len(Jay - Machine) == len(Emily - Machine):
    print("무승부입니다!")

else:
    print("잘못된 값입니다!")