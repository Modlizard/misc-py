import os
import random
import time

os.system('color 0a')

#0-6: Tanks | 7-22: Damage | 23-28: Support
heroes = ['Sigma', 'D.Va', 'Orisa', 'Reinhardt', 'Roadhog', 'Winston', 'Wrecking Ball', 'Zarya', 'Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'Mei', 'Pharah', 'Reaper', 'Soldier: 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker', 'Ana', 'Baptiste', 'Brigitte', 'Lucio', 'Mercy', 'Moira', 'Zenyatta']

endProgram = False

print("""|Random Overwatch Hero Generator|
-By Modlizard\n""")

while endProgram == False:
    time.sleep(0.25)
    heroSet = input('Would you like a tank, damage, support or any? T/D/S/A: ').upper()
    if heroSet == 'T':
        hero = heroes[random.randint(0,7)]
        print('-'*len(hero)*2)
        print(hero)
        print('-'*len(hero)*2)
    elif heroSet == 'D':
        hero = heroes[random.randint(8,23)]
        print('-'*len(hero)*2)
        print(hero)
        print('-'*len(hero)*2)
    elif heroSet == 'S':
        hero = heroes[random.randint(24,30)]
        print('-'*len(hero)*2)
        print(hero)
        print('-'*len(hero)*2)
    elif heroSet == 'A':
        hero = heroes[random.randint(0,30)]
        print('-'*len(hero)*2)
        print(hero)
        print('-'*len(hero)*2)
    else:
        print('Invalid option!')
        
