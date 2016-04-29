"""
[5th problem]
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

start       1205
break-start 1243
break-end   1548
end         1556
= 50min
"""


def calc(op_list, vals=[1, 2, 3, 4, 5, 6, 7, 8, 9], vals_str=["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
    if len(op_list) == 0:
        return vals[0], vals_str[0]

    if "" in op_list:
        i = op_list.index("")
        vals = vals[:i] + [op(vals[i], vals[i+1], op_list[i])] + vals[i+2:]
        vals_str = vals_str[:i] + [op(vals_str[i], vals_str[i+1], op_list[i], False)] + vals_str[i+2:]
        op_list = op_list[:i] + op_list[i+1:]
        return calc(op_list, vals, vals_str)

    vals = [op(vals[0], vals[1], op_list[0])] + vals[2:]
    vals_str = [op(vals_str[0], vals_str[1], op_list[0], False)] + vals_str[2:]
    op_list = op_list[1:]
    return calc(op_list, vals, vals_str)


def op(a, b, o, val=True):
    if o == "":
        return int(str(a) + str(b)) if val else "{}{}".format(a, b)
    if o == '+':
        return a + b if val else "{}+{}".format(a, b)
    if o == '-':
        return a - b if val else "{}-{}".format(a, b)


def get_all_cadidates():
    all_cadidates = []

    def dfs(c=0, l=[]):
        if c == 8:
            all_cadidates.append(l)
            return
        for o in ["", "+", "-"]:
            dfs(c+1, l + [o])
        return

    dfs()
    return all_cadidates


if __name__ == "__main__":
    all_cadidates = get_all_cadidates()
    for cadidates in all_cadidates:
        v, s = calc(cadidates)
        if v == 100:
            print s
