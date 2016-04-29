"""
[2nd problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start 11:35
end   11:40
= 5min
"""


def combile_list(list1, list2):
    t1, t2 = len(list1), len(list2)
    i, j = 0, 0
    ret = []
    while i < t1 or j < t2:
        if i < t1:
            ret.append(list1[i])
        if j < t2:
            ret.append(list2[j])
        i += 1
        j += 1

    return ret


if __name__ == '__main__':
    print combile_list(["a", "b", "c"], [1, 2, 3])
    print combile_list(["a", "b", "c", "d", "e"], [1, 2, 3])
