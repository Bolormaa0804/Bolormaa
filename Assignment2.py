# Bolormaa Munkhzaya
# CSC 115
# Assignment 2
# 02/06/2022
# Dice Game
import math
import random
print("  Welcome to Dice Game\n")
print("     ____")
print("    /'  .\    _____")
print("   /: \___\  / .  /\ ")
print("   \' / . / /____/..\ ")
print("    \/___/  \'  '\  / ")
print("             \'__'\/")

print("Rule: You are given $250 to start.")
print("You cannot play once you run out of money.")
print("There will be two dice and you have to guess the sum of two dice.")
print("The winning amount is twice the bet. If you lose you lose the amount of your bet.")
money = 250
while True:
    bet = int(input("How much are you betting?: "))
    if bet > money:
        print("Sorry your balance is lower than your bet. Try again with valid amount.")
        bet = int(input("How much are you betting?: "))
    print("Rolling the dice....")
    ans = int(input("What is the sum of the two dice? "))
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("Die 1 is", dice1)
    print("Die 2 is", dice2)
    total = dice1 + dice2
    if ans == total:
        award = bet * 2
        print("You win $", award)
        money += award
    else:
        money -= bet
        print("You lost $", bet)
    print("Your current balance is $", money)
    if money == 0:
        print("Sorry you are out of money.")
        print("See you later!")
        break
    choice = input("Do you want another game? y/n: ")
    if choice == 'n':
        print("See you again!")
        break
    else:
        continue

    print("\n")



