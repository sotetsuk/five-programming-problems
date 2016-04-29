"""
[1st problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start 11:28
end   11:35
= 7min
"""


def sum_for(l):
    sum = 0
    for e in l:
        sum += e
    return sum


def sum_while(l):
    sum = 0
    i = 0
    len_l = len(l)
    while i < len_l:
        sum += l[i]
        i += 1
    return sum


def sum_recur(l):
    if l is None:
        return 0
    return l[0] if len(l) == 1 else l[0] + sum_recur(l[1:])


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print sum_for(l)
    print sum_while(l)
    print sum_recur(l)
