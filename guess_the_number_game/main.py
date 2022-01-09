#Number Guessing Game Objectives:
import art
import random

def get_allowed_guesses(selected_choice):  
  return 5 if selected_choice == "hard" else 10

def check_the_number(computers_number, user_number):
  if user_number == computers_number:
    return 0
  elif user_number < computers_number:
    print("Too low")
  elif  user_number > computers_number:
    print("Too high") 
  
  return -1

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("Pssst, the correct answer is 62")
choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
allowed_guesses = get_allowed_guesses(choice)

computer_guess = random.randint(1,100)
remaining_guesses = allowed_guesses

number_guessed = False
while remaining_guesses > 0:
  print(f"You have {remaining_guesses} attempts to guess the number.")
  user_guess = int(input("Make a guess:"))
  if check_the_number(computer_guess, user_guess) == -1:
    remaining_guesses -= 1
  else:    
    number_guessed = True
    remaining_guesses = 0

if number_guessed:
  print(f"You got it! The answer was {computer_guess}.")
else:
  print(f"Sorry! Your have no more attempts available to guess!! The answer was {computer_guess}")