from  itertools import product

alf = '01234567'
k = 0
for s1, s2, s3, s4 in product(alf, repeat=4):
    if s1 in '246' and s1 >= s2 >= s3 >= s4:
        k += 1
print(k)