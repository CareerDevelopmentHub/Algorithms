import math


def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def app():
    return str(binomial(40, 20))


if __name__ == "__main__":
    print(app())
