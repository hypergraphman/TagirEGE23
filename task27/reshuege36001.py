f = open('27b.txt')
n = int(f.readline())
data = []
for _ in range(n):
    p1, p2 = map(int, f.readline().split())
    if p1 % 2:
        data.append((max(p1, p2), min(p1, p2)))
print(data)
s_b = sum(map(lambda x: x[0], data))
s_m = sum(map(lambda x: x[1], data))
print(s_b)
print(s_m)
print(s_b + s_m)
data.sort(key=lambda x: x[0] + x[1])
print(*data[:10])