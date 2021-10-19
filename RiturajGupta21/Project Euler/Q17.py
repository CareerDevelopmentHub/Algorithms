def app():
    res = sum(len(cte(i)) for i in range(1, 1001))
    return str(res)


def cte(n):
    if 0 <= n < 20:
        return one[n]
    elif 20 <= n < 100:
        return ten[n // 10] + (one[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return one[n // 100] + "hundred" + (("and" + cte(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return cte(n // 1000) + "thousand" + (cte(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError()


one = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
       "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ten = ["", "", "twenty", "thirty", "forty",
       "fifty", "sixty", "seventy", "eighty", "ninety"]


if __name__ == "__main__":
    print(app())
