def f(num):
    k = 0
    while num % 2 == 0:
        k += 1
        num //= 2
    if k > 10:
        k = 10
    return k


n, *a = map(int, open('27-B.txt'))

b = [[0] * 11 for _ in range(3)]

k = 0
for el in a:
    t = f(el)
    for i in range(10 - t, 11):
        k += b[-(el % 3)][i]
    b[el % 3][t] += 1

print(k)
# 2005090253