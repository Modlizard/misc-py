from random import randint
from os import system
arr = "»--->"
output = ''
lineCount = [3,3,3,3,3,4,4,4,5,5]
spaceCount = [1,1,2,2,2,2,3,3,4,4]
arrowCount = [1,2,2,3,3,3,3,4,4,5]
for line in range(lineCount[randint(0,9)]):
    for arrow in range(arrowCount[randint(0,9)]):
        output += ' '*spaceCount[randint(0,9)] + arr
    output += '\n'

print(output)
system('pause')