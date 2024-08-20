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


import random
#taking user input
print("Choose a number between 1,2 and 3 where they represent scissors rock and paper respectively")
user_input=int(input())
print(f"your input is {user_input} which gives you...")
if user_input==1:
    print(scissors)
    print("scissors")
elif user_input==2:
    print(rock)
    print("rock")
elif user_input==3:
    print(paper)
    print("paper")

computer_input= random.randint(1,3)
print(computer_input)
print("Computer got...")
if computer_input==1:
    print(scissors)
    print("scissors")
elif computer_input==2:
    print(rock)
    print("rock")
elif computer_input==3:
    print(paper)
    print("paper")

# #rules of the game
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
if computer_input==user_input:
    print("Its a draw")
elif user_input==1  and computer_input==3:
    print("You Won")
elif user_input==2 and computer_input==1:
    print("You Won")
elif user_input==3 and computer_input==2:
    print("You won")
else:
    print("You Lose")