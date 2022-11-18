from itertools import permutations

afl = 'kkap'
words = set()
for word in permutations(afl):
    word = ''.join(word)
    words.add(word)

print(len(words))