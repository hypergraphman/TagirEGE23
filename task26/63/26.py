f = open('26-62.txt')
n, v = map(int, f.readline().split())
a = []
for _ in range(n):
    cost, good = f.readline().split()
    cost = int(cost)
    a.append((cost, good))
a.sort(key=lambda x: (x[0], -int(x[1], 36)))
print(a)
k = 0
res = []
while v >= a[k][0]:
    v -= a[k][0]
    res.append(a[k])
    k += 1
print(k, v)
while True:
    if a[k][1] == 'Z':
        find = None
        for i in range(len(res) - 1, -1, -1):
            if res[i][1] == 'Q':
                find = res[i]
                break
        if not find:
            break
        if find[0] + v >= a[k][0]:
            res.remove(find)
            res.append(a[k])
            v -= a[k][0] - find[0]
        else:
            break
    k += 1
c = 0
for el in res:
    if el[1] == 'Z':
        c += 1
print(c, v)
