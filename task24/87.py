with open('test.txt') as f:
    s = f.read()
nums = []
d = ''
for el in s:
    if el.isdigit():
        d += el
    else:
        if d:
            nums.append(int(d))
        d = ''
if d:
    nums.append(int(d))
print(max(filter(lambda x: x % 2, nums)))
