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

#Write your code below this line 👇

game_options = ["rock", "paper", "scissors"]
game_display = [rock, paper, scissors]
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if (user_pick < 0 or user_pick > 2):
  print("You picked an invalid number, You loose!!")
else:
  computer_pick = random.randint(0,2)

  print(f"You picked: {game_options[user_pick]} {game_display[user_pick]}")
  print(f"Computer picked: {game_options[computer_pick]} {game_display[computer_pick]}")


  if user_pick == computer_pick:
    print("Its a tie!!")
  else:
    user_wins = True
    if user_pick == 0 and computer_pick == 1:
      user_wins = False
    elif user_pick == 1 and computer_pick == 2:
      user_wins = False
    elif user_pick == 2 and computer_pick == 0:
      user_wins = False

    if user_wins == True:
      print("You win! Congratulations!!")
    else:
      print("Sorry, Computer wins!!")



