from collections import defaultdict
d = defaultdict(int)
f = open('27_type B.txt')
n = int(f.readline())
k = int(f.readline())
a = []
for _ in range(n):
    num_p, val_p = map(int, f.readline().split())
    a.append((num_p, val_p))
    # a.append(tuple(map(int, f.readline().split())))

t = a[:k]
mx = 0
for i in range(k, len(a)):
    num_p, val_p = a[i]
    num_p_left, val_p_left = t[i % k]
    if val_p_left > d[num_p_left]:
        d[num_p_left] = val_p_left
    if d[num_p]:
        mx = max(d[num_p] + val_p, mx)
    t[i % k] = a[i]
print(mx)
