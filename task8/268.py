from itertools import product

alf = '02461111'
k = 0
for s in product(alf, repeat=5):
    word = ''.join(s)
    if word[0] != '0' and word.count('6') == 1 and '61' not in word and '16' not in word:
        k += 1
print(k)