import sys


class memoize:

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            val = self.func(*args)
            self.cache[args] = val
            return val


def app():
    sys.setrecursionlimit(3000)
    res = max(range(1, 1000000), key=ccl)
    return str(res)


@memoize
def ccl(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return ccl(y) + 1


if __name__ == "__main__":
    print(app())
