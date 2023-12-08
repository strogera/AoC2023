from math import lcm

with open("input.txt", "r") as inputFile:
    instructiont, elemsInit =  inputFile.read().split('\n\n')
    elems = {}
    for line in elemsInit.split('\n'):
        key, steps = line.split(' = ')
        steps = steps.replace('(', '').replace(')', '').split(', ')
        elems[key] = steps

    i = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        for ins in instructiont:
            i += 1
            curr = elems[curr][0] if ins == 'L' else elems[curr][1]
    print(i)

    curr = [x for x in elems if x[2] == 'A']
    i = 0
    firstMet = {}
    while len(firstMet) != len(curr):
        for inst in instructiont:
            i += 1
            for j in range(len(curr)):
                curr[j] = elems[curr[j]][0] if inst == 'L' else elems[curr[j]][1]
                if curr[j][2] == 'Z' and j not in firstMet:
                    firstMet[j] = i
            
    print(lcm(*firstMet.values()))
