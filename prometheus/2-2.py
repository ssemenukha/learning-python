import sys
import math
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

song = "Everybody sing a song:"
words = ' '.join(str(e) for e in [ "-".join(["la"] * x )  for a in range(y) ])
if z == 1:
    final = words + "!"
else:
    final = words + "."

print song, final