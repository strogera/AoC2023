from itertools import combinations

def expand(grid, delta=2):
    galaxies = set()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "#":
                galaxies.add((x, y))

    galaxiesNew = [[g[0], g[1]] for g in galaxies]
    for x, line in enumerate(grid):
        if all(c == "." for c in line):
            for i, g in enumerate(galaxies):
                if g[0] > x:
                    galaxiesNew[i][0] += delta - 1

    for x, line in enumerate(zip(*grid)):
        if all(c == "." for c in line):
            for i, g in enumerate(galaxies):
                if g[1] > x:
                    galaxiesNew[i][1] += delta - 1

    return galaxiesNew


def calcDistances(galaxies):
    return sum(
        abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in combinations(galaxies, 2)
    )


with open("input.txt", "r") as inputFile:
    grid = [line.strip() for line in inputFile.readlines()]
    print(calcDistances(expand(grid)))
    print(calcDistances(expand(grid, 1_000_000)))
