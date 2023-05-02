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

#Write your code below this line 👇
import random

comp_chose = random.randint(0, 2)
cases = [rock, paper, scissors]
user_chose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if user_chose <3 and user_chose >= 0:
  print("Computer chose:")
  print(cases[comp_chose])
  print("You chose:")
  print(cases[user_chose])
if user_chose == comp_chose:
    print("It is a draw")
elif user_chose < 0 or user_chose >= 3:
    print("You typed a invalid number, you lose!")
elif user_chose == 0 and comp_chose == 2:
    print("Hurrah.....You won!!")
elif user_chose == 1 and comp_chose == 0:
    print("Hurrah.....You won!!")
elif user_chose == 2 and comp_chose == 1:
    print("Hurrah.....You won!!")
else:
    print("Shit.....you lose")
