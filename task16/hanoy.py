def hanoy(q, f, t, b):
    if q == 0:
        return
    hanoy(q - 1, f, b, t)
    print(f'переместили диск {q} c штыря {f} на штырь {t}')
    hanoy(q - 1, b, t, f)


hanoy(4, 1, 3, 2)