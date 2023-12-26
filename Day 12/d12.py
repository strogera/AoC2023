from functools import cache


@cache
def num_solutions(s, sizes, num_done_in_group=0):
    # https://github.com/fuglede/adventofcode/blob/master/2023/day12/solutions.py
    if not s:
        return not sizes and not num_done_in_group
    num_sols = 0
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            num_sols += num_solutions(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += num_solutions(s[1:], sizes[1:])
            else:
                num_sols += num_solutions(s[1:], sizes)
    return num_sols


with open("input.txt", "r") as inputFile:
    s = 0
    s2 = 0
    for line in inputFile.readlines():
        temp = line.strip().split(" ")
        nums = tuple(int(x) for x in temp[1].split(","))
        s += num_solutions(temp[0] + ".", nums)
        s2 += num_solutions("?".join([temp[0]] * 5) + ".", nums * 5)
    print(s)
    print(s2)
