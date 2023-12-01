numsStr = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def partOne(inp):
    s = 0
    for line in inp:
        nums = [c for c in line if c.isdigit()]
        s += int(nums[0] + nums[-1])
    return s

def partTwo(inp):
    inp2 = []
    for line in inp:
        newline = line
        for n in numsStr:
            newline = newline.replace(n, n[0] + numsStr[n] + n[-1])
        inp2.append(newline)
    return partOne(inp2)

with open("input.txt") as inputFile:
    inp = inputFile.readlines()
    print(partOne(inp))
    print(partTwo(inp))
