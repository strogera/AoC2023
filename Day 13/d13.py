def vertical(grid, diff=0):
    return horizontal(list(zip(*grid)), diff)


def horizontal(grid, diff=0):
    for b in range(len(grid) - 1):
        i, j = b, b + 1
        countDifferences = 0
        while countDifferences <= diff and i >= 0 and j < len(grid):
            for k in range(len(grid[i])):
                if grid[i][k] != grid[j][k]:
                    countDifferences += 1
            i -= 1
            j += 1
        if countDifferences == diff:
            return b + 1
    return 0


with open("input.txt", "r") as inputFile:
    grids = [grid.split("\n") for grid in inputFile.read().split("\n\n")]
    print(sum(vertical(grid) + 100 * horizontal(grid) for grid in grids))
    print(sum(vertical(grid, 1) + 100 * horizontal(grid, 1) for grid in grids))
