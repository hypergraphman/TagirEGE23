*a, = map(int, open('17-37344.txt').read().split())
res = [a[i] + a[j] for i in range(len(a) - 1) for j in range(i + 1, len(a)) if a[i] * a[j] % 10 == 0]
print(len(res), max(res))