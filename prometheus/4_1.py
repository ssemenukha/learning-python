import sys

instring = sys.argv[1].lower().replace(" ","")
if instring == instring[::-1]:
    print "YES"
else:
    print "NO"