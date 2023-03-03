from collections import defaultdict

with open('') as f:
    s = f.read()

lines = s.split()
find_line = ''
mx = 0
for line in lines:
    cur_len = 1
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            cur_len += 1
            if cur_len > mx:
                mx = cur_len
                find_line = line
        else:
            cur_len = 1

statist = defaultdict(int)
for el in find_line:
    statist[el] += 1

char = max(statist.items(), key=lambda x: x[1])[0]
print(s.count(char), char)