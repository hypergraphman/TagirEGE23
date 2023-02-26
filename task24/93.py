with open('test.txt') as f:
    s = f.read()
mx_len = 1
cur_len = 1
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        cur_len += 1
        mx_len = max(cur_len, mx_len)
    else:
        cur_len = 1
print(mx_len)