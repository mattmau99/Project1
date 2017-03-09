from re import *
from time import sleep
from subprocess import run
from time import sleep


def math():
    try:
        question1 = int(input("What is 1 + 1?\nAnswer: "))
    except ValueError:
        question1 = input("Please enter your answer again: ",)
    if question1 == 2:
        print("You got a point!")
    else:
        print("Incorrect.")

    
def tivia():
    print("Not yet complete.")
def cleanup():
    print("Now, let's clean up this screen for you.")
    sleep(2)
    ready = input("Are you ready? Yes or No?\nAnswer: ")
    if match(r'[yY][eE][sS]', ready):
        print("Alright here we go.")
        run(['clear'])
    elif match(r'[nN][oO]', ready):
        cleanup()
    else:
        print("Invalid input. We will do it anyway")
        run(['clear'])
    input("Press Enter to continue.",)
    
print("This is a game")
sleep(2)
print("You have to win this game.")
sleep(2)
print("If you do not win this game it will bug you a lot.")
sleep(2)
try:
    squareroot = int(input("Quick! What's the square root of 64!?!?!?!?!?\nAnswer: ",))
except ValueError:
    squareroot = input("Please enter the same thing: ",)
print("I was just messing with you.")

sleep(2)
if squareroot == 8:
    print("But, you did get it right! Congratulations!")
else:
    print("You did get it wrong though. It is 8.")
    sleep(2)
    print("You said {}". format(squareroot))

sleep(2)
print("You will do a series of challenges. Unlike any you have ever done before.")
sleep(2)
print("Multiple choice questions like these:")
sleep(2)
input("How are you today?\n1) Good\n2) Bad\nAnswer: ",)
sleep(2)
print("Or non-multiple choice questions like this:")
sleep(2)
input("How are you today?\nAnswer: ",)
sleep(2)
understanding = input("Do you understand? Yes or No\nAnswer: ",)
sleep(2)
if match(r'[yY][eE][sS]', understanding):
    print("Good, let's move on.")
elif match(r'[nN][oO]', understanding):
    print("When you have a multiple choice question, you enter the number that it corresponds to.")
    sleep(2)
    print("Otherwise, you just type in your answer.")
    sleep(2)
    print("If you don't understand now, I am not giving you another explanation, you will catch on.")
else: 
    print("Invalid Answer, you will never know")

cleanup()

sleep(2)
print("Now we will start the challenges.")
try:
    challenge = int(input("1) Math\n2) Trivia\nAnswer: ",))
except ValueError:
    challenge = input("Enter your answer again. ",)
if challenge == 1:
    math()
elif challenge == 2:
    trivia()
else:
    print("Invalid Answer.")