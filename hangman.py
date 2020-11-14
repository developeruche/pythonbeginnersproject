################################
#Carryiing out all importation
################################
import random

#-------------------------------

################################
#Stating all the Functions Here.
################################
def hagman():
    word = random.choice(["water", "stack", "nutter", "ballon", "lion", "cat", "father", "mother", "classes", "fireman", "ironman", "components", "python", "javascript"])
    validCharaters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessMade = ""
    
    while len(word) > 0: 
        main = ""
        missed = 0

        for letter in word:
            if letter in guessMade:
                main = main + letter
            else: 
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win!!!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validCharaters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid character.")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left.")
                print("  ---------  ")
            if turns == 8: 
                print("8 turns left.")
                print(" ----------  ")
                print("      0      ")
            if turns == 7: 
                print("7 turns left.")
                print(" ----------  ")
                print("      0      ")
                print("      |      ")
            if turns == 6: 
                print("6 turns left.")
                print(" ----------  ")
                print("      0      ")
                print("      |      ")
                print("     /      ")
            if turns == 5: 
                print("5 turns left.")
                print(" ----------  ")
                print("      0      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4: 
                print("4 turns left.")
                print(" ----------  ")
                print("    \ 0      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3: 
                print("3 turns left.")
                print(" ----------  ")
                print("    \ 0 /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2: 
                print("2 turns left.")
                print(" ----------  ")
                print("    \ 0 /|    ")
                print("      |      ")
                print("     / \     ")
            if turns == 1: 
                print("Lat breath counting.")
                print(" ----------  ")
                print("    \ 0 _|/    ")
                print("      |      ")
                print("     / \     ")
            if turns == 0: 
                print("You lose!!!")
                print(" ----------  ")
                print("      0_|    ")
                print("    / | \    ")
                print("     / \     ")
                break
            


name = input("Please Enter your name... ")
print("Welcome ", name)
print("-_-_-_-_-_-_-_-_-_-")
print(name , "Try to guess this word in less than 10 trials.")
hagman()