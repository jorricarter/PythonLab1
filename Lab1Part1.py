import random
#todo computer thinks of random number
randomNumber = random.randint(1, 10)
#todo ask user to guess number in range
currentGuess = int(input ("Guess a number between 1 and 10\n"))
#todo take INTEGER input from user
#made previous line more efficient.
#todo notify user of too high or too low
while currentGuess != randomNumber:
    if currentGuess > randomNumber:
        print("Your guess was too high!")
    if currentGuess < randomNumber:
        print("Your guess was too low!")
    currentGuess = int(input("Guess again!\n"))
print ("You got it!")
