def north(grid):
    for x, line in enumerate(grid):
        for i, c in enumerate(line):
            if c == "O":
                j = x
                while j - 1 >= 0 and grid[j - 1][i] not in "#O":
                    j -= 1
                grid[x][i] = "."
                grid[j][i] = "O"
    return grid


def count(grid):
    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                s += len(grid) - i
    return s


def rotate_matrix(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []
    for row in transposed:
        rotated.append(row[::-1])
    return rotated


def cycle(grid):
    for _ in range(4):
        grid = north(grid)
        grid = rotate_matrix(grid)
    return grid


def cachable(grid):
    return "".join(["".join(x) for x in grid])


with open("input.txt", "r") as inputFile:
    grid: list = [list(line.strip()) for line in inputFile.readlines()]
    print(count(north(grid)))

    cache = {}
    step = 1_000_000_000
    i = 0
    foundCycle = False
    st = 1
    while i < step:
        grid = cycle(grid)
        i += 1
        if not foundCycle and cachable(grid) in cache:
            c = i - cache[cachable(grid)]
            i += c * ((step - i) // c)
            foundCycle = True
        else:
            cache[cachable(grid)] = i
    print(count(grid))
