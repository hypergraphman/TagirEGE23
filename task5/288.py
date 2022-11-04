def alg(n):
    s = f'{n:b}'
    if (n % 2) == 0:
        s = '1' + s + '10'
    else:
        s = '11' + s + '0'
    return int(s, 2)


a = set()
i = 0
b = 0
for i in range(1000):
    if 800 <= alg(i) <= 1500:
        a.add(alg(i))
print(len(a))