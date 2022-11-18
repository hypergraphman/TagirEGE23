from itertools import permutations

alf = 'NAB'
k = 0
for w in permutations(alf):
    k += 1
print(k)

alf = '1234'
m = 0
for w in permutations(alf):
    m += 1
print(k * m, k, m)
