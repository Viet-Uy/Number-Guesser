import random #Importing random to access the .randint function for the game

#Function for choosing difficulty for the game
def difficultyChooser(difficulty):
    if difficulty == 1:
        print("Easy difficulty chosen (1,10) \n")
        return randomNumberGenerator(1,10)
    elif difficulty == 2:
        print ("Medium difficulty chosen (1,100) \n")
        return randomNumberGenerator(1,100)
    elif difficulty == 3:
        print ("Hard difficulty chosen (1,1000) \n")
        return randomNumberGenerator(1,1000)
    else: 
        print("Not an eligible difficulty!")
        return None

#Random numbergenerator returning a value based on the difficulty
def randomNumberGenerator(a,b):
    return random.randint(a,b)

randomNumber = None
checker = True
while checker:
    if randomNumber == None:
        try:
            playerPreference = input("What difficulty do you want? \n1.Easy \n2.Medium \n3.Hard \n")
            randomNumber = difficultyChooser(int(playerPreference)) #Making the number into an integer, if not possible then catch the error and have them repeat
            if randomNumber == None:
                continue
        except ValueError:
            print("Not a valid option!")
            continue
    else:
        try:
            #Allows the player to guess the number
            playerGuess = int(input("Which number is the program thinking about? \n"))
            #Difference to help pinpoint the number by telling them if they are close or not
            difference = abs(randomNumber - playerGuess)

        except ValueError:
            print("Please enter a valid number! \n")
            continue

        #If the player guesses right
        if playerGuess == randomNumber:
            print("Congratulations!")

            #While loop that continues to loop until they get a valid answer either yes or no
            while True:
                restart = (input("Do you want to play again? (y/n) \n").strip()).lower()
                if restart == "y" or restart == "yes":
                    #If yes, make randomNumber = None so the whole process can start from scratch.
                    randomNumber = None
                    #Break out of the while True loop
                    break 
                elif restart == "n" or restart == "no":
                    #checker = False if they decide to not play anymore, disabling the main while-loop
                    checker = False 
                    print("Goodbye! \n")
                    break
                else:
                    #If any other answer is given, repeat the while True loop to get the desired answer
                    print("Try again! \n")
            continue
        
        #If the difference is off by over 3, then it tells them they are way of. Scaling based on difficulty is possible.
        
        elif playerGuess > randomNumber:
            if difference >= 3:
                print("Your number is way too high! \n")
            else:
                print("Your number is too high \n")
        
        elif playerGuess < randomNumber:
            if difference >=3:
                print("Your number is way too low! \n")
            else:
                print("Your number is too low \n")
    
