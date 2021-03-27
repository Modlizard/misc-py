#Made for the password module in Keep Talking and Nobody Explodes
#Program by Modlizard

###Base variable definition
spaceOne = []
spaceTwo = []
spaceThree = []
spaceFour = []
spaceFive = []
words = ["about", "after", "again", "below", "could",
         "every", "first", "found", "great", "house",
         "large", "learn", "never", "other", "palce",
         "plant", "point", "right", "small", "sound",
         "spell", "still", "study", "their", "there",
         "these", "thing", "think", "three", "water",
         "where", "which", "world", "would", "write"]
countSpace = 1
countLetter = 1

###Input mechanism
for space in [spaceOne,spaceTwo,spaceThree,spaceFour,spaceFive]:
    for letter in range(6):
        space.append(input("Enter letter "+str(countLetter)+" of space "+str(countSpace)+": "))
        countLetter += 1
    countLetter = 1
    countSpace += 1
countSpace = 1
for space in [spaceOne,spaceTwo,spaceThree,spaceFour,spaceFive]:
    print("Space", countSpace, space)
    countSpace += 1

###Cracking mechanism
for a in spaceOne:
    for b in spaceTwo:
        for c in spaceThree:
            for d in spaceFour:
                for e in spaceFive:
                    for x in words:
                        testWord = a+b+c+d+e
                        if testWord == x:
                            print("THE WORD IS", testWord)
                            break
                        else:
                            pass
                        
