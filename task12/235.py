s = '>' + '1' * 10 + '2' * 20 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>')
    s = s.replace('>2', '2>')
    s = s.replace('>3', '1>')
print(s)
print(sum(map(int, s[:-1])))