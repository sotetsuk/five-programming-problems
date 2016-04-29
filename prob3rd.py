"""
[3rd problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start 11:41
end   11:53
= 12min
"""


def fib():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    f = fib()
    for i, n in enumerate(f):
        if i > 10:
            break
        print n
