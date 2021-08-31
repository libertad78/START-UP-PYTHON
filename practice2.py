sentence = input("이름을 입력하세요 : ")
print(sentence)

print(sentence[0])
print(sentence[-1])
print(sentence[2:6])

print(sentence + sentence)
print(sentence * 3)
print(sentence, sentence)

word = sentence + sentence
word2 = sentence * 4

print(word)
print(word2)

print(sentence.count('u'))
print(sentence.lstrip())
print(sentence.rstrip())
print(sentence.strip())
print(sentence.upper())
print(sentence.lower())
print(sentence.index('u'))
print(sentence.replace('u','a'))