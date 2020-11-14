import random
print("Hello there, I am thinking of a number try guessing it...")
print("You have 6 trials")
print("By the way what is your name?")
name = input()
print("nice to meet you ", name)
upperBound = int(input("Choose an Upper bound greater than zero"))
quizNumber = random.randint(1, upperBound)
for guessMade in range(1, upperBound + 1):
    userGuess = int(input("Take a guess between 0 -" + str(upperBound)))
    if(userGuess > quizNumber):
        print("You guessed higher")
    elif(userGuess < quizNumber):
        print("You guessed Lower...")
    else:
        break
if(userGuess == quizNumber):
    print("You win!!! Hurray...")
else:
    print("You lose...")