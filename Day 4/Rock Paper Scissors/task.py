import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


userChoice = int(input("What do you choose? Type 0 for Rock or 1 for Scissors, and 2 for Paper \n"))

computerChoice = random.randint(0,2)

if userChoice == 0:
    print(rock)

    if computerChoice == 0:
        print("The computer chose:")
        print(rock)
        print("Its a draw brother")
    elif computerChoice == 1:
        print("The computer chose:")
        print(scissors)
        print("You win brother great choice")
    else:
        print("The computer chose:")
        print("Bad choice brother, you lose")

elif userChoice == 1:
    print(scissors)

    if computerChoice == 0:
        print("The computer chose:")
        print(rock)
        print("Bad choice brother, you lose")
    elif computerChoice == 1:
        print("The computer chose:")
        print(scissors)
        print("Its a draw brother")
    else:
        print("The computer chose:")
        print("Great choice brother, you win")

else:
    print(paper)

    if computerChoice == 0:
        print("The computer chose:")
        print(rock)
        print("You win brother great choice")
    elif computerChoice == 1:
        print("The computer chose:")
        print(scissors)
        print("Bad choice brother, you lose")
    else:
        print("The computer chose:")
        print("It's a tie brother")


