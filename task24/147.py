from collections import defaultdict

s = 'ASDBASDTGWEQGFDASASDTRQEWRGASDSDARTQREGASDFFAQWEFASDF'
dd = defaultdict(int)
for i in range(len(s) - 1):
    if s[i] == 'A':
        dd[s[i + 1]] += 1
mx = 0
ans = ''
for key in sorted(dd.keys()):
    if dd[key] > mx:
        mx = dd[key]
        ans = key
print(ans)