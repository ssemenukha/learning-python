import sys
import math
x = float(sys.argv[1])
m = float(sys.argv[2])
d = float(sys.argv[3])

f = (1 / (d * math.sqrt(2 * math.pi))) * math.exp( -1 * ((( x - m )**2) / (2 * d**2) ))

print f
