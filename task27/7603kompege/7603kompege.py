n, k, *data = map(int, open('27B_7603.txt'))
temp, left_max, i, mx = data[:k], -float('inf'), 0, -float('inf')
for el in data[k:]:
    left_max = max(temp[i], left_max)
    mx = max(left_max + el, mx)
    temp[i] = el
    i = (i + 1) % k
print(mx)