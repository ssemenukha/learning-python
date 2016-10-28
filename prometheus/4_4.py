import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
tot = 0
for n in range(a1, a2+1):
    num = "0" * (6 - len(str(n))) + str(n)
    p1 = p2 = 0
    c = 0
    while c < 6:
        if c < 3:
            p1 += int(num[c])
        else:
            p2 += int(num[c])
        c += 1
    if p1 == p2:
        tot += 1
print tot