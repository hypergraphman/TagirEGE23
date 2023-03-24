n, *a = map(int, open('26-45.txt').read().split())
s = set(a)
res = []
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0 and (a[i] + a[j]) // 2 in s:
            res.append((a[i] + a[j]) // 2)
print(len(res), max(res))
