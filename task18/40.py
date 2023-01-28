a = [int(x) for x in open('40.txt').readlines()]
print(a)

cur_len = 0
max_len = 0
for el in a:
    if el % 2:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len)