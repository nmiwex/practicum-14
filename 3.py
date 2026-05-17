words_num = int(input())
dictionary = {}

for _ in range(words_num):
    couple = input().split()
    dictionary[couple[0]] = couple[1]

word = input()
if word in dictionary:
    print(dictionary[word])
elif word in dictionary.values():
    for key in dictionary:
        if dictionary[key] == word:
            print(key)
else:
    print(word)
