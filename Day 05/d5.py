def getLocation(seed, maps):
    cur = seed
    for m in maps:
        for c in m:
            if c[1] <= cur < c[1] + c[2]:
                cur = c[0] + cur - c[1]
                break
    return cur


with open("input.txt", "r") as inputFile:
    inp = inputFile.readlines()
    seeds = list(map(int, inp[0].split(": ")[1].strip().split(" ")))
    maps = []
    for line in inp:
        if line == "\n":
            maps.append([])
        elif ":" not in line:
            destStart, sourceStart, length = map(int, line.strip().split())
            maps[-1].append((destStart, sourceStart, length))

    ans = 999999999999
    for s in seeds:
        ans = min(ans, getLocation(s, maps))
    print(ans)

    ans = 999999999999
    step = 10000
    origSeed = 0
    for i in range(0, len(seeds), 2):
        for s in range(seeds[i], seeds[i] + seeds[i + 1], step):
            cur = getLocation(s, maps)
            if cur < ans:
                origSeed = s
                ans = cur
        for s in range(origSeed - step, origSeed + step + 1):
            ans = min(ans, getLocation(s, maps))
    print(ans)
