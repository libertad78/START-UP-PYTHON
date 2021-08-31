sentence = input("원화를 입력하세요 : ")
print(sentence)

euro = 1/1360
pound = 1/1576
dollar = 1/1153
yen = 1/10
wen = 1/177

sentence2 = "원은"

e_w = euro * int(sentence)
p_w = pound * int(sentence)
d_w = dollar * int(sentence)
y_w = yen * int(sentence)
w_w = wen * int(sentence)

print(sentence, sentence2, e_w, "유로 입니다")
print(sentence, sentence2, p_w, "파운드 입니다")
print(sentence, sentence2, d_w, "달러 입니다")
print(sentence, sentence2, y_w, "엔 입니다")
print(sentence, sentence2, w_w, "위안 입니다")

