s = open('24febsg.txt').readlines()
mx = 0
ans = 0
for line in s:
    cur_len = 1
    mx_len = 1
    ch = line[0]
    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            cur_len += 1
            if cur_len > mx_len:
                mx_len = cur_len
                ch = line[i]
        else:
            cur_len = 1
    if mx_len > mx:
        mx = mx_len
        ans = line.count(ch)
    if mx_len == mx and line.count(ch) > ans:
        ans = line.count(ch)
print(ans)
