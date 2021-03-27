advTpFile = open('homes.yml', 'r')
lineOrder = [1,5,2,3,4,6,7]
currentFile = open('dummy.txt','w+')
file = advTpFile.read()
homes = file.split('\n')
for x in range(0,len(homes)):
    if homes[x][0] != ' ': #If first char isn't a space then it's a new UUID
        currentFile.close()
        currentUUID = homes[x].replace(':','') #Removes colon from UUID
        currentFile = open(currentUUID+".yml", 'a+')
        currentFile.write('homes:\n')
        for y in lineOrder:
            currentFile.write(homes[x+y]+'\n') #Copies 7 lines in the correct rearranged order into the new file
            print(homes[x+y]) #Debug
        cooldown = 7
    else:
        if cooldown != 1: #Don't write to file for the next 7 lines because they were all written in advance
            cooldown -= 1
        else:
            try: #Checking or copying the next line when already on the final one raises an error
                if homes[x+1][0] != ' ': #If the next line is a new UUID don't copy the next 7 line segment over
                    pass
                else:
                    for y in lineOrder:
                        currentFile.write(homes[x+y]+'\n')
                        print(homes[x+y]) #Debug
                    cooldown = 7
            except:
                print('End of file.')
currentFile.close()
