from itertools import product

for i in range(3 + 1):
    z = product('0123456789', repeat=i)
    for v in z:
        s = int('1234' + ''.join(v) + '7')
        if s % 141 == 0:
            print(s, s // 141)