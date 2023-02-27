from math import log
from random import randint
# 0.15% rare fish, 10% uncommon fish, 34.85% common fish, 55% trash

totals = {'common': 0, 'uncommon': 0, 'rare': 0, 'trash': 0}
upperLimit = 2*10**6
formatWdith = int(round(log(upperLimit, 10)+1, 0))
for x in range(0,upperLimit):
    roll = randint(0,9999)
    if roll < 15:
        totals['rare'] += 1
    elif roll < 3500:
        totals['common'] += 1
    elif roll < 4500:
        totals['uncommon'] += 1
    else:
        totals['trash'] += 1
    if (x + 1) % (upperLimit//20) == 0:
        print("[{rolls:<{width}} Rolls]".format(rolls=x+1, width=formatWdith), end=" ")
        for n in totals:
            print("{}: {:<{width}} {:<10}".format(n.title(), totals[n], "("+str(round(totals[n]*100/(x+1), 4))+"%)", width=formatWdith), end=" ")
        print()