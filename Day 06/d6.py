from math import prod


def join(l):
    return int("".join(map(str, l)))


def race(t, d):
    c = 0
    for v in range(t):
        if v * (t - v) > d:
            c += 1
    return c


with open("input.txt", "r") as inputFile:
    t = list(map(int, inputFile.readline().split(":")[1].split()))
    d = list(map(int, inputFile.readline().split(":")[1].split()))

    print(prod([race(t1, d1) for t1, d1 in zip(t, d)]))
    print(race(join(t), join(d)))
