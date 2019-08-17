# Jessica Alexander
# 06/19/2019
# Trivia Game

PlayerName = input("Player Name: ")
def displayMenu():
    valid = False
    while not valid:
        print("   ************************************************************")
        print("*  Welcome To Jessica's Random Trivia Game!! ;)  *")
        print("   ************************************************************")
        print("Menu")
        print("1. Music Trivia")
        print("2. 80s Movie Trivia")
        print("3. Given Trivia")
        print()
        menuChoice = input("Please chose an option from the above menu: ")
        if menuChoice == "1":
            triviaFile = open ("Music.txt", "r", errors  = 'ignore')
            NameOfFile = triviaFile.readline()
            print("****************")
            print(NameOfFile)
            print("****************")
            print("****************")
            print("*Welcome", PlayerName, "*")
            print("****************")
            valid = True
        elif menuChoice == "2":
            triviaFile = open ("80sMovies.txt", "r", errors  = 'ignore')
            NameOfFile = triviaFile.readline()
            print("****************")
            print(NameOfFile)
            print("****************")
            print("****************")
            print("*Welcome", PlayerName, "*")
            print("****************")
            valid = True
        elif menuChoice == "3":
            triviaFile = open ("Given.txt", "r", errors  = 'ignore')
            NameOfFile = triviaFile.readline()
            print("****************")
            print(NameOfFile)
            print("****************")
            print("****************")
            print("*Welcome", PlayerName, "*")
            print("****************")
            valid = True
        else:
            print("That was not a valid option. Please try again. ")
    return triviaFile

def next_inquiry (triviaFile):
    retort = triviaFile.readline()
    inquiry = triviaFile.readline()
    inquiry = inquiry.replace("/", "\n")
    result1 = triviaFile.readline()
    result2 = triviaFile.readline()
    result3= triviaFile.readline()
    result4= triviaFile.readline()
    RightAnswer = triviaFile.read(1)
    triviaFile.readline()
    reason = triviaFile.readline()
    reason = reason.replace("/", "\n")
    marks = triviaFile.readline()
    return retort, inquiry, result1, result2, result3, result4, RightAnswer, reason, marks

def gameRound(triviaFile):
    totalMarks = 0
    retort, inquiry, result1, result2, result3, result4, RightAnswer, reason, marks = next_inquiry (triviaFile)
    while retort:
        print(retort)
        print(inquiry)
        print("1.", result1)
        print("2.", result2)
        print("3.", result3)
        print("4.", result4)
        print()
        answerChoice = input("Please choose the correct answer: ")
        if answerChoice == RightAnswer:
            print("That is correct!")
            print()
            print(reason)
            print("You earned", marks)
            totalMarks += int(marks)
        else:
            print("I'm sorry that's not correct.")
            print("The correct answer is: ", RightAnswer)
            print(reason)
            print()
        retort, inquiry, result1, result2, result3, result4, RightAnswer, reason, marks = next_inquiry (triviaFile)

    print()
    print(PlayerName, "your total marks are: ", totalMarks)
    triviaFile.close()

#main
triviaFile = displayMenu()
gameRound(triviaFile)
done = False
answer = "y"
while not done:
    answer = input("Would you like to play another round?(y or n)")
    if answer == "y" or answer == "Y":
        triviaFile = displayMenu()
        gameRound(triviaFile)
    else:
        print()
        print("Thank you ", PlayerName, " for playing, see you next time!")
        done = True
