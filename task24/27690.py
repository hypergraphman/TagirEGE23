s = open('24.txt').read()

mx = 1
cur_len = 1
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cur_len += 1
        if cur_len > mx:
            mx = cur_len
    else:
        cur_len = 1
print(mx)