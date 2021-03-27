string = input('Enter the string you wish to compress: ')
compressed = '' #Result variable initialisation
character = string[0] #Character being analysed
frequency = 0 #How many times it was repeated
for x in string: #Each character in the string
    if x == character:
        frequency += 1
    else:
        compressed += character + ' ' + str(frequency) + ' '
        character = x #The current character being analysed is updated
        frequency = 1 #This is its first occurence

compressed += character + ' ' + str(frequency) + ' ' #The final group is concatenated onto the end of the result
print('Here is your compressed string:', compressed)

