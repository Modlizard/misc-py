#Calculates amount of boxes you can buy with provided amount
boxCost = 15111.59
bal = 0
print("Change the actual code to determine what box you're opening, current box cost:", boxCost)
while bal != -1:
    bal = float(input("Enter your balance: "))
    boxAmount = bal/boxCost
    print(int(boxAmount), "boxes")
    print("("+str(round(boxAmount, 6))+")")
