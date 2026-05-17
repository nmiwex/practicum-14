words_num = int(input())
dictionary = {}

for _ in range(words_num):
    couple = input().split()
    dictionary[couple[0]] = couple[1]

text = input().split()
translated_text = ''

for word in text:
    if word in dictionary:
        translated_text += dictionary[word] + ' '
    else:
        translated_text += word + ' '

print(translated_text)