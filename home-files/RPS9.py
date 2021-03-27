from random import randint

sentences = ["Rock pounds out fire!","Rock crushes scissors!","Rock crushes human!","Rock crushes sponge!",
             "Fire melts scissors", "Fire burns paper", "Fire burns human", "Fire burns sponge",
             "Scissors swish through air", "Scissors cut paper", "Scissors cut human", "Scissors cut sponge",
             "Human cleans with sponge", "Human writes paper", "Human breathes air", "Human drinks water",
             "Sponge soaks paper", "Sponge uses air pockets", "Sponge absorbs water", "Sponge cleans gun",
             "Paper fans air", "Paper covers rock", "Paper floats on water", "Paper outlaws gun",
             "Air blows out fire", "Air erodes rock", "Air evaporates water", "Air tarnishes gun",
             "Water erodes rock", "Water puts out fire", "Water rusts scissors", "Water rusts gun",
             "Gun targets rock", "Gun targets fire", "Gun outclasses scissors", "Gun shoots human"]
             
itemBeats = {"rock": {"fire": 0, "scissors": 1, "human": 2, "sponge": 3}, #Rock beats fire, scissors, human, sponge
         "fire": {"scissors": 4, "human": 6, "sponge": 7, "paper": 5},
         "scissors": {"human": 10, "sponge": 11, "paper": 9, "air": 8},
         "human": {"sponge": 12, "paper": 13, "air": 14, "water": 15},
         "sponge": {"paper": 16, "air": 17, "water": 18, "gun": 19},
         "paper": {"air": 20, "water": 22, "gun": 23, "rock": 21},
         "air": {"water": 26, "gun": 27, "rock": 25, "fire": 24},
         "water": {"gun": 31, "rock": 28, "fire": 29, "scissors": 30},
         "gun": {"rock": 32, "fire": 33, "scissors": 34, "human": 35}}

items = ["rock", "fire", "scissors", "human", "sponge", "paper", "air", "water", "gun"]

def vsAI():
    print("1 - Rock\n2 - Fire\n3 - Scissors\n4 - Human\n5 - Sponge\n6 - Paper\n7 - Air\n8 - Water\n9 - Gun")
    invalidInput = True
    while invalidInput == True:
        selection = int(input("Enter a number from 1-9 to select your item: "))
        if selection > 9 or selection < 1:
            print("Invalid input")
        else:
            invalidInput = False
    selectedItem = items[selection-1] #Player's item
    print("\nYou selected", selectedItem)

    aiSelection = randint(0,8) #Computer's item
    aiItem = items[aiSelection]
    print("The AI selected", aiItem)

    if aiItem in itemBeats[selectedItem].keys(): #If computer's item is in the list of stuff your item beats
        print("\n"+sentences[itemBeats[selectedItem][aiItem]], "\nYou win!")
    elif aiItem == "human" and selectedItem == "human":
        print("\nYou both chose human, because of the way this game works neither of you win and this is marked as a draw. If one of the humans is female and the other is male then you could potentially do something but leave that out of this program ( ͡° ͜ʖ ͡°)")
    elif aiItem == selectedItem: #If you both chose the same
        print("\nYou both chose the same item, everyone's disappointed, you draw and literally nothing happens. So fun.")
    else:
        print("\n"+sentences[itemBeats[aiItem][selectedItem]], "\nYou lose!")
    
def vsHuman():
    print("[Player 1]\n1 - Rock\n2 - Fire\n3 - Scissors\n4 - Human\n5 - Sponge\n6 - Paper\n7 - Air\n8 - Water\n9 - Gun")
    invalidInput = True
    while invalidInput == True:
        selection = int(input("Enter a number from 1-9 to select your item: "))
        if selection > 9 or selection < 1:
            print("Invalid input")
        else:
            invalidInput = False
    selectedItem = items[selection-1] #Player's item

    print("\n[Player2]\n1 - Rock\n2 - Fire\n3 - Scissors\n4 - Human\n5 - Sponge\n6 - Paper\n7 - Air\n8 - Water\n9 - Gun")
    invalidInput = True
    while invalidInput == True:
        selection2 = int(input("Enter a number from 1-9 to select your item: "))
        if selection2 > 9 or selection < 1:
            print("Invalid input")
        else:
            invalidInput = False
    selectedItem2 = items[selection2-1] #Player's item
    print("\nPlayer 1 selected", selectedItem)
    print("Player 2 selected", selectedItem2)

    if selectedItem2 in itemBeats[selectedItem].keys(): #If computer's item is in the list of stuff your item beats
        print("\n"+sentences[itemBeats[selectedItem][selectedItem2]], "\nYou win!")
    elif selectedItem2 == "human" and selectedItem == "human":
        print("\nYou both chose human, because of the way this game works neither of you win and this is marked as a draw. If one of the humans is female and the other is male then you could potentially do something but leave that out of this program ( ͡° ͜ʖ ͡°)")
    elif selectedItem2 == selectedItem: #If you both chose the same
        print("\nYou both chose the same item, everyone's disappointed, you draw and literally nothing happens. So fun.")
    else:
        print("\n"+sentences[itemBeats[selectedItem2][selectedItem]], "\nYou lose!")

def vsMultipleAI():
    print("1 - Rock\n2 - Fire\n3 - Scissors\n4 - Human\n5 - Sponge\n6 - Paper\n7 - Air\n8 - Water\n9 - Gun")
    invalidInput = True
    while invalidInput == True:
        selection = int(input("Enter a number from 1-9 to select your item: "))
        if selection > 9 or selection < 1:
            print("Invalid input")
        else:
            invalidInput = False
    selectedItem = items[selection-1] #Player's item
    games = ""
    invalidInput = True
    while invalidInput == True:
        games = input("How many games should be generated: ")
        if games.isdigit():
            print(games, "Games will be generated.")
            invalidInput = False
        else:
            print("Invalid number, it has to be a positive integer; try again.")
    
    for x in range(0,int(games)):
        aiSelection = randint(0,8) #Computer's item
        aiItem = items[aiSelection]
        print("\nThe AI selected", aiItem)
        
        if aiItem in itemBeats[selectedItem].keys(): #If computer's item is in the list of stuff your item beats
            print(sentences[itemBeats[selectedItem][aiItem]], "[You win!]")
        elif aiItem == "human" and selectedItem == "human":
            print("You both chose human, because of the way this game works neither of you win and this is marked as a draw. If one of the humans is female and the other is male then you could potentially do something but leave that out of this program ( ͡° ͜ʖ ͡°) [You draw!]")
        elif aiItem == selectedItem: #If you both chose the same
            print("You both chose the same item, everyone's disappointed, you draw and literally nothing happens. So fun. [You draw!]")
        else:
            print(sentences[itemBeats[aiItem][selectedItem]], "[You lose!]")

def main():
    invalidInput = True
    while invalidInput == True:
        mode = input("Would you like to play with an AI (enter 'a'), another player (enter 'p') or multiple games against an ai (enter 'm'): ").lower()
        if mode == 'a':
            invalidInput = False
            vsAI()
        elif mode == 'p':
            invalidInput = False
            vsHuman()
        elif mode == 'm':
            invalidInput = False
            vsMultipleAI()
        else:
            print("Invalid input, try again.")

main()
