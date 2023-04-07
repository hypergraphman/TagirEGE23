from collections import defaultdict

f = open('26-92.txt')
n = int(f.readline())
d = defaultdict(set)
for _ in range(n):
    row, pix, z = f.readline().split()
    row = int(row)
    pix = int(pix)
    if z == '+':
        d[row].add(pix)
    else:
        if pix in d[row]:
            d[row].remove(pix)
n_row, mx_count = 0, 0
for row in sorted(d.keys()):
    t = sorted(d[row])
    cur_len, max_len = 1, 1
    for i in range(len(t) - 1):
        if t[i] + 1 == t[i + 1]:
            cur_len += 1
            max_len = max(cur_len, max_len)
        else:
            cur_len = 1
    if max_len >= mx_count:
        mx_count = max_len
        n_row = row
print(mx_count, n_row)
