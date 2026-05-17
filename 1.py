text = input().lower().split()
words = {}

for word in text:
    words[word] = text.count(word)

sorted_words = sorted(words, key=lambda x: words[x], reverse=True)
for word in sorted_words:
    print(word)