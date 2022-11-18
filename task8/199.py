from itertools import product

alf = (1, 2, 3, 4, 5)
# alf = 'aedcb'
# d = {'a': 0, 'e': 1, 'd': 2, 'c': 3, 'b': 4}
k = 0
for t in product(alf, repeat=4):
    # if d[t[0]] <= d[t[1]] <= d[t[2]] <= d[t[3]]:
    if t[0] <= t[1] <= t[2] <= t[3]:
        k += 1
print(k)
