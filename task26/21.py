v, n, *a = map(int, open('26-k1.txt').read().split())
a.sort(reverse=True)
print(a[n])
print(sum(a[:n]) * 0.2)