def divs(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


print(len(divs(107864)), divs(107864))
