#STONE,PAPER,CISOR(proj1)

import random

user_input=input("Enter either 's', 'p' or 'c' : ")
print("you entered :",user_input)

possible_option = ['s','p','c']
computer_input = random.choice(possible_option)
print("computer entered :",computer_input)

if(user_input == computer_input):
    print("This is tie match")
elif user_input == 's':
    if computer_input == 'c':
        print("You are the winner")
    else:
        print("Computer is the winner!")
elif user_input == 'p':
    if computer_input == 'c':
        print("computer is  the winner")
    else:
        print("you are the winner!")
elif user_input == 'c':
    if computer_input == 's':
        print("computer is the winner")
    else:
        print("you ar the winner!")


