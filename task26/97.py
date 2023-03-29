f = open('26-97.txt')
n = int(f.readline())
a = []
for line in f.readlines():
    d, t = map(int, line.split())
    a.append((d, d - 2 * t - 3))
a.sort(key=lambda x: -x[1])
prev = a[0][1]
tubes = [a[0]]
for d1, d2 in a:
    if d1 <= prev:
        prev = d2
        tubes.append((d1, d2))
mx = 0
for d1, d2 in a:
    if d1 <= tubes[-2][1] and d1 > mx:
        mx = d1
print(len(tubes), mx)