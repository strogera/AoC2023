def makeOperation(x, m, a, s, w, workFlows):
    w = workFlows[w]
    for cw in w.split(','):
        if cw == 'A':
            return True
        elif cw == 'R':
            return False
        elif ':' not in cw:
            return makeOperation(x, m ,a, s, cw, workFlows)
        first, sec = cw.split(':')
        if eval(first):
            return makeOperation(x, m , a, s, sec, workFlows)


with open("input.txt", "r") as inputFile:
    parts = {}
    parts['A'] = 'A'
    parts['R'] = 'R'
    accepted = (0)
    pa, workFlows = inputFile.read().split("\n\n")
    for s in pa.splitlines():
        name, rest  = s.split("{")
        parts[name] = rest.strip()[:-1]

    ans = 0
    for p in workFlows.splitlines():
        x, m, a, s = p.replace("{", "").replace("}", "").split(',')
        x, m, a, s = int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])
        if makeOperation(x, m, a, s, 'in', parts):
            ans += sum([x, m, a, s])
            accepted = (x, m, a, s)
    print(ans)

    import re

splits = {c: [0, 4000] for c in 'xmas'}

for c,o,v in re.findall(r'(\w+)(<|>)(\d+)', pa):
    splits[c].append(int(v)-(o=='<'))


ranges = lambda x: [(a,a-b) for a,b in zip(x[1:], x)]
X,M,A,S = [ranges(sorted(splits[x])) for x in splits]

C = 0
for i, (x,dx) in enumerate(X):
    for m,dm in M:
        for a,da in A:
            for s,ds in S:
                if makeOperation(x, m, a, s, 'in', parts):
                    C += dx * dm * da * ds

print(C)