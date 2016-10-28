import sys
instr = sys.argv[1]
pos = instr.find("()")
while pos != -1 and instr != "":
    instr = instr.replace("()", "")
    pos = instr.find("()")

if instr == "":
    print "YES"
else:
    print "NO"