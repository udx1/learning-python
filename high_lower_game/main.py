import art
import game_data
import random
import os

user_score = 0
wrong_answer = False
MAX_GAMES = len(game_data.data)

# Returns the game data from the dictionary.
def get_game_data(pos):
  return f"{game_data.data[pos]['name']}, {game_data.data[pos]['description']}, {game_data.data[pos]['country']} "
  
# Check user selection.
def is_wrong_answer(pos1, pos2, user_selection):
  pos1_count = game_data.data[pos1]["follower_count"]
  pos2_count = game_data.data[pos2]["follower_count"]

  if (pos1_count > pos2_count and user_selection == pos1):
    return False
  elif(pos1_count < pos2_count and user_selection == pos2):
    return False    
  else:
    return True

# Start with a random option A.
option_a = random.randint(0,MAX_GAMES-1)
while not wrong_answer:
  game_data_a = get_game_data(option_a)

  os.system('clear')
  print(art.logo)
  if user_score > 0:
    print(f"You are right! Current score: {user_score}")
  print(f"Compare A: {game_data_a}")
  print(art.vs)
  # get the random option B
  option_b = random.randint(0,MAX_GAMES-1)

  # if the random turned out to be same as A, get a different one.
  while option_b == option_a:  
    option_b = random.randint(0,MAX_GAMES-1)
  game_data_b = get_game_data(option_b)
  print(f"Against B: {game_data_b}")
  user_selection = input("Who has more Instagram followers? Type 'A' or 'B':").lower()
  user_selected_option = option_a if user_selection == 'a' else option_b 
  wrong_answer = is_wrong_answer(option_a, option_b, user_selected_option)
  if not wrong_answer:
    user_score +=1
    option_a = user_selected_option
    print(f"You are right! Current score: {user_score}")
  else:
    print(f"Sorry, that's wrong. Final score: {user_score}")
