import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = ''

phrase = sys.argv[1].replace(" ", "")

for i in range(0,(len(phrase) // 5) * 5,5):
    code = ''
    for j in range(i,i + 5):
        if phrase[j] == phrase[j].lower():
            code = code + "a"
        else:
            code = code + "b"
    answer = answer + alphabet[ key.find(code) ]
    
print answer