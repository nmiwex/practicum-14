words_num = int(input())
dictionary = {}

for _ in range(words_num):
    string = input().split()
    dictionary[string[0]] = string[1:]

word = input()

for key in dictionary:
    if word in dictionary[key]:
        print(key)