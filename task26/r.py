v, n, *a = map(int, open('26.txt').read().split())

a.sort()
k = 0
while v - a[k] >= 0:
    v -= a[k]
    k += 1
print(k)
v += a[k - 1]
mx = a[k - 1]
while v >= a[k]:
    mx = a[k]
    k += 1
print(mx)
print(max(filter(lambda x: x <= v, a)))
