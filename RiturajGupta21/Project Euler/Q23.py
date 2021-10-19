def app():
    n = 28124
    dsum = [0] * n
    for i in range(1, n):
        for j in range(i * 2, n, i):
            dsum[j] += i
    num = [i for (i, x) in enumerate(dsum) if x > i]

    exp = [False] * n
    for i in num:
        for j in num:
            if i + j < n:
                exp[i + j] = True
            else:
                break

    res = sum(i for (i, x) in enumerate(exp) if not x)
    return str(res)


if __name__ == "__main__":
    print(app())
