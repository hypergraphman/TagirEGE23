from itertools import permutations

alf = 'krbl'
k = 0
for w in permutations(alf, r=3):
    k += 1
print(k)

alf = 'oai'
m = 0
for w in permutations(alf, r=3):
    m += 1
print(m)
print(k * m)
