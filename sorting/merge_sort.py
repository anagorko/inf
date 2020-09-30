def merge(l, p):
    i = iter(l)
    j = iter(p)

    r = list()

    n = next(i, None)
    m = next(j, None)

    while n is not None or m is not None:
        if n is not None and m is not None:
            if n < m:
                r.append(n)
                n = next(i, None)
            else:
                r.append(m)
                m = next(j, None)
        elif n is not None:
            r.append(n)
            n = next(i, None)
        else:
            r.append(m)
            m = next(j, None)
    return r


def sort(l):
    if len(l) > 1:
        return merge(sort(l[:len(l)//2]), sort(l[len(l)//2:]))

    return l


print(sort([1, 2, 3, 0, 0, 0, 0, 0, 0]))
