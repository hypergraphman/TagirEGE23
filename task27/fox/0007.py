f = open('27_B.txt')
n = int(f.readline())
a = []
k = 25
for _ in range(n):
    km, bottle = map(int, f.readline().split())
    a.append((km, (bottle + k - 1) // k))

for i in range(550065, 550085):
    s = 0
    for j in range(n):
        s += abs(a[i][0] - a[j][0]) * a[j][1]
    print(i, s)
# 73094 A
# 9162792129264 B
