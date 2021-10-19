def app():
    dsum = [0] * 10000
    for i in range(1, len(dsum)):
        for j in range(i * 2, len(dsum), i):
            dsum[j] += i

    res = 0
    for i in range(1, len(dsum)):
        j = dsum[i]
        if j != i and j < len(dsum) and dsum[j] == i:
            res += i
    return str(res)


if __name__ == "__main__":
    print(app())
