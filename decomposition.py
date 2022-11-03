def decomp(n):
    n = factorial(n)
    d = 2
    count = 0
    dct = {}
    while d * d <= n:
        if n % d == 0:
            count += 1
            n //= d
        else:
            if count != 0:
                dct[d] = count
            count = 0
            d += 1
    if n > 1:
        dct[d] = count
        dct[n] = 1
    string = ''
    for i in dct:
        if dct[i] > 1:
            string += str(i) + '^' + str(dct[i]) + ' * '
        else:
            string += str(i) + ' * '
    return string.rstrip(' * ')


def factorial(n):
    a = 1
    b = 1
    while a != n:
        b = b * a
        a += 1
    b *= n
    return b