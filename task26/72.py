f = open('26-72.txt')
n, m, k = map(int, f.readline().split())

d = dict()
for i in range(1, m + 1):
    d[i] = [0, n + 1]

for _ in range(k):
    row, num = map(int, f.readline().split())
    d[row].append(num)

c = 0
n_row = 0
mx_s = 0
for row in d.keys():
    s = 0
    d[row].sort()
    for left, right in zip(d[row], d[row][1:]):
        t = right - left - 4
        if t > 0:
            s += t
    c += s
    if s > mx_s:
        mx_s = s
        n_row = row
print(c, n_row)
