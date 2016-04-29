"""
[4th problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start 11:54
end   12:02
= 8min
"""


def largest_num(l):
    """
    We can use greedy method

    :param l:
    :return:
    """

    l_str = [str(e) for e in l]
    l_str.sort()
    ret = "".join(l_str[::-1])

    return int(ret)


if __name__ == '__main__':
    print largest_num([50, 2, 1, 9])
