from collections import defaultdict
from math import lcm

i = 0

def button(rxPresses= {}):
    global i
    i += 1
    p = 1
    low = 1 + len(mods['roadcaster'])
    high = 0
    q = []
    for d in mods['roadcaster']:
        q.append((0, 'roadcaster', d))

    while q:
        p, src, mod = q.pop(0)

        if mod == 'rx':
            continue

        newp = 0
        if mod in conj:
            conj[mod][src] = p
            if (any(n == 0 for n in conj[mod].values())):
                newp = 1

        if mod in flipflops:
            if p == 1:
                continue
            flipflops[mod] = not flipflops[mod]
            if flipflops[mod]:
                newp = 1

        if newp == 1:
            high += len(mods[mod])
        else:
            low += len(mods[mod])

        for d in mods[mod]:
            q.append((newp, mod, d))

        for m, pulse in conj[rxParent].items():
            if pulse == 1 and m not in rxPresses:
                rxPresses[m] = i
    return (low, high)




with open("input.txt", "r") as inputFile:
    mods = defaultdict(list)
    conj = {}
    flipflops = {}
    rxParent = ''
    for line in inputFile.readlines():
        m, rest = line.strip().split('->')
        if 'rx' in rest:
            rxParent = m[1:].strip()
        rest = rest.split(',')
        mods[m.strip()[1:]] = [x.strip() for x in rest]
        if m[0] == '%':
            flipflops[m[1:].strip()] = False
        elif m[0] == '&':
            conj[m[1:].strip()] = {}


    for k, dest in mods.items():
        for d in dest:
            if d in conj:
                conj[d][k] = 0

    ans = (0, 0)
    for _ in range(1000):
        low, high = button()
        ans = (ans[0] + low, ans[1] + high)
    print(ans[0]*ans[1])

    rxPresses = {}
    while len(rxPresses) < 4:
        button(rxPresses)
    print(lcm(*rxPresses.values()))

        
