from math import prod

with open("input.txt", "r") as inputFile:
    cubesAvailable = {"red": 12, "green": 13, "blue": 14}
    ans1, ans2 = 0, 0
    for line in inputFile.readlines():
        minCubesRequired = dict.fromkeys(cubesAvailable, 0)
        id, rest = line.split(":")
        id = int(id.split(" ")[-1])
        for cube in rest.strip().replace(";", ",").split(","):
            v, k = map(str.strip, cube.strip().split(" "))
            v = int(v)
            if cubesAvailable[k] < v:
                id = 0
            if v > minCubesRequired[k]:
                minCubesRequired[k] = v
        ans1 += id
        ans2 += prod(minCubesRequired.values())

    print(ans1)
    print(ans2)
