from itertools import product

alf = 'егэ'
c = 0
for letters in product(alf, repeat=5):
    word = ''.join(letters)
    if word[0] in 'еэ':
        c += 1
print(c)