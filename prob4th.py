"""
[4th problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start 11:54
end   12:02
= 8min

After I solved all problems, I found that the greedy solution is wrong.
So I fixed using permutations and it took almost 10min.
"""

from itertools import permutations


def largest_num(l):
    m = -1
    for e in permutations(l):
        m = max(int("".join([str(x) for x in e])), m)

    return m

if __name__ == '__main__':
    print largest_num([50, 2, 1, 9])
    print largest_num([50, 5, 56])
