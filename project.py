# Name: Anastasia Iogova and Bolormaa Munkhzaya
# Class: CSC 115
# Date: April 28 2022
# Python Group Project
# File Name: CSC115 GroupProject Version3.py


# This is the third version of our code.
# We have implemented reading the program responses from a file.


import random

# read from the file of responses


def readFile():
    inFile = open("responseFile.txt", "r")
    fileContents = inFile.read().split("&")
    inFile.close()
    return fileContents

# function that responds to 'hello'


def greeting(fileContents):
    responseList = fileContents[0].split(":")
    response = random.choice(responseList)
    print(response)

# function that responds to 'how are you'


def howAreYou(fileContents):
    responseList = fileContents[1].split(":")
    response = random.choice(responseList)
    print(response)

# function that reponds to 'what is your name'


def name(fileContents):
    responseList = fileContents[2].split(":")
    response = random.choice(responseList)
    print(response)

# function that reponds to 'what is your favorite color'


def favoriteColor(fileContents):
    responseList = fileContents[3].split(":")
    response = random.choice(responseList)
    print(response)

# function that reponds to 'what is your favorite food'


def favoriteFood(fileContents):
    responseList = fileContents[4].split(":")
    response = random.choice(responseList)
    print(response)

# function that responds to 'what is your favorite animal'


def favoriteAnimal(fileContents):
    responseList = fileContents[5].split(":")
    response = random.choice(responseList)
    print(response)

# function that responds to 'do you have any pets'


def pets(fileContents):
    responseList = fileContents[6].split(":")
    response = random.choice(responseList)
    print(response)

# function that responds to 'how old are you'


def age(fileContents):
    responseList = fileContents[7].split(":")
    response = random.choice(responseList)
    print(response)

# function that responds to 'who is the best computer science professor'


def bestProfessor(fileContents):
    responseList = fileContents[8].split(":")
    response = random.choice(responseList)
    print(response)

# function that reponds to 'what is your favorite programming language'


def programmingLanguage(fileContents):
    responseList = fileContents[9].split(":")
    response = random.choice(responseList)
    print(response)


def main():
    # introduction
    print("Welcome. My name is PyBot.")
    print("I'm here to be your virtual friend.")
    print("Type 'quit','done', or 'bye' when you no longer want to talk.")

    print('''
Here are the things you can say to me:
1. Hello / Hi / Hey
2. How are you?
3. What is your name? / Who are you?
4. What is your favorite color?
5. What is your favorite food?
6. What is your favorite animal?
7. Do you have any pets?
8. How old are you?
9. Who is the best computer science professor?
10. What is your favorite programming language?''')

    # the main loop of the program
    while True:
        # get user input
        userInput = input("\nSay something: ").lower().strip(" !?.,")
        fileContents = readFile()

        # selection that decides which function to call
        match userInput:
            case "hello" | "hi" | "hey":
                greeting(fileContents)
            case "how are you":
                howAreYou(fileContents)
            case "what is your name" | "who are you":
                name(fileContents)
            case "what is your favorite color":
                favoriteColor(fileContents)
            case "what is your favorite food":
                favoriteFood(fileContents)
            case "do you have any pets":
                pets(fileContents)
            case "how old are you":
                age(fileContents)
            case "who is the best computer science professor":
                bestProfessor(fileContents)
            case "what is your favorite programming language":
                programmingLanguage(fileContents)
            case "quit" | "done" | "bye":
                break
            case _:
                print("Sorry, I have not been programed to understand what you just said.")

    print("\nGoodbye!")


main()
