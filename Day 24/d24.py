import z3

class Hail:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.l = (vel[1]/vel[0])
        self.trajPart1 = pos[1] - self.l * pos[0]

with open("input.txt", "r") as inputFile:
    hails = []
    for line in inputFile.read().splitlines():
        inp = [int(x.strip()) for y in line.split('@') for x in y.split(',') ]
        hails.append(Hail(inp[:3], inp[3:]))
        
    count = 0
    for i, h in enumerate(hails):
        for j in range(i + 1, len(hails)):
            if hails[i].l == hails[j].l:
                # parallel
                continue
            x = (hails[j].trajPart1 - hails[i].trajPart1)/(hails[i].l - hails[j].l)
            y = x * hails[i].l + hails[i].trajPart1
            a = (x - hails[i].pos[0])/hails[i].vel[0]
            b = (x - hails[j].pos[0])/hails[j].vel[0]
            if a >= 0 and b >= 0 and x >= 200000000000000 and x <= 400000000000000 and y >= 200000000000000 and y <= 400000000000000:
                count += 1
    print(count)


x, y, z = z3.Real('x'), z3.Real('y'), z3.Real('z')
vx, vy, vz = z3.Real('vx'), z3.Real('vy'), z3.Real('vz')

s = z3.Solver()

for i, h in enumerate(hails):
	(ax, ay, az), (vax, vay, vaz) = h.pos, h.vel

	t = z3.Real(f't_{i}')
	s.add(t >= 0)
	s.add(x + vx * t == ax + vax * t)
	s.add(y + vy * t == ay + vay * t)
	s.add(z + vz * t == az + vaz * t)

assert s.check() == z3.sat

m = s.model()
x, y, z = m.eval(x), m.eval(y), m.eval(z)
x, y, z = x.as_long(), y.as_long(), z.as_long()

print(x + y + z)



