import sys

n = int(sys.argv[1])
sum = 0
prev = 0
preprev = 1
for i in range(1,n+1):
    sum = prev + preprev
    preprev = prev
    prev = sum
print sum