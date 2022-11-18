from itertools import permutations

alf = 'улей'
for letters in permutations(alf, r=4):
    word = ''.join(letters)
    print(word)