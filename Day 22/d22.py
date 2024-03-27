from collections import defaultdict

def toPoint(s):
    return [int(x) for x in s.split(',')]

def dropBrick(heights, brick):
    maxSeenHeight = max(heights[(x, y)] for x in range(brick[0][0], brick[1][0] + 1) for y in range(brick[0][1], brick[1][1] + 1))
    dist = brick[0][2] - maxSeenHeight - 1
    dist = 0 if dist < 0 else dist
    return ([brick[0][0], brick[0][1], brick[0][2] - dist],[brick[1][0], brick[1][1], brick[1][2] - dist]), dist


def dropAll(bricks):
    heights = defaultdict(int)
    nBricks = []
    fallenBricks = 0
    for b in bricks:
        droppedBrick, dist= dropBrick(heights, b)
        fallenBricks += 1 if dist > 0 else 0
        nBricks.append(droppedBrick)
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                heights[(x, y)] = droppedBrick[1][2]
    return fallenBricks, nBricks

with open("input.txt", "r") as inputFile:
    bricks = []
    for line in inputFile.readlines():
        a, b = line.strip().split('~')
        bricks.append((toPoint(a), toPoint(b)))

    _, bricks = dropAll(sorted(bricks, key=lambda k: k[0][2]))
    ans1 = 0
    ans2 = 0
    for i, _ in enumerate(bricks):
        disint = bricks[:i] + bricks[i+1:]
        cf, _ = dropAll(disint)
        ans1 += 1 if cf == 0 else 0
        ans2 += cf 
    print(ans1)
    print(ans2)
