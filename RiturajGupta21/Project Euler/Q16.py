def app():
    n = 2**1000
    res = sum(int(c) for c in str(n))
    return str(res)


if __name__ == "__main__":
    print(app())
