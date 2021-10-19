import itertools


def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y


def app():
    tri = 0
    for i in itertools.count(1):
        tri += i
        if nd(tri) > 500:
            return str(tri)


def nd(n):
    e = sqrt(n)
    res = sum(2
              for i in range(1, e + 1)
              if n % i == 0)
    if e**2 == n:
        res -= 1
    return res


if __name__ == "__main__":
    print(app())
