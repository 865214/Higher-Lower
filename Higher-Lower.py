##################################### Higher-Lower-Game ############################################################
# Importing modules
from art import logo,vs # Importing logos from other files 
from replit import clear # Importing clear() from replit libraries
from game_data import data # Importing data from games_data file
import random # Importing random_module 
# Creating higher_lower() function and creating necessary opetaions 
def higher_lower():
  game = True # we are defining game fucntion which is True because we are using while loop
  score = 0 # Initially score is 0 if the user choses correct answer then it will be added by 1
  print(logo) # Printing logo
  random_selection1 = random.choice(data) # Using random module to choice random elements from the list
# we are printing the first element of the data from the list. But it is in dictionary format. So we are tapping key to print our value
  print(f"Compare A : {random_selection1['name']}, a {random_selection1['description']}, from {random_selection1['country']}") 
  print(vs) # print vs logo
# we are printing the first element of the data from the list. But it is in dictionary format. So we are tapping key to print our value
  random_selection_2 = random.choice(data)
  print(f"Against B : {random_selection_2['name']} , a {random_selection_2['description']}, from {random_selection_2['country']}")
  while game: # We are using while loop
# We are giving the option to user they should type A or else Type B
    user = input("Who has more followers?: Type 'A' or 'B': ").lower()
# If user choses A then if the first element follower is greater than second element then it will add up to the score by 1 and then they will feedback the user that how much user has score continously. if they given the wrong answer they give the feed back how much they score and also if the user chooses correct answer then the second element becomes first element and vice versa
    if user == 'a':
      if random_selection1['follower_count'] > random_selection_2['follower_count']:
        game = True
        score +=1
        clear()
        print(logo)
        print(f"You're right,current Score: {score}")
        random_selection1 = random_selection_2
        print(f"Compare A : {random_selection1['name']}, a {random_selection1['description']}, from {random_selection1['country']}")
        print(vs)
        random_selection_2 = random.choice(data)
        print(f"Against B : {random_selection_2['name']} , a {random_selection_2['description']}, from {random_selection_2['country']}")
      else:
        clear()
        print(logo)
        print(f'sorry you did it wrong, final_score: {score}')
        game = False
# If user choses B then if the first element follower is greater than second element then it will add up to the score by 1 and then they will feedback the user that how much user has score continously. if they given the wrong answer they give the feed back how much they score and also if the user chooses correct answer then the second element becomes first element and vice versa
    elif user == 'b':
      if random_selection1['follower_count'] > random_selection_2['follower_count']:
        game = True
        score +=1
        clear()
        print(logo)
        print(f"You're right,current score: {score}")
        random_selection1 = random_selection_2
        print(f"Compare A : {random_selection1['name']}, a {random_selection1['description']}, from {random_selection1['country']}")
        print(vs)
        random_selection_2 = random.choice(data)
        print(f"Against B : {random_selection_2['name']} , a {random_selection_2['description']}, from {random_selection_2['country']}")
      else:
        clear()
        print(logo)
        print(f'sorry you did it wrong, final_score: {score}')
        game = False
higher_lower()
# we are giving user an option they want to restart the game again. if they type Y then it will clear the previous game and start an new game again
while input("Do you want to Try Again: Type 'Y' to retry or 'N' to exit: ").lower()=='y': 
  clear()
  higher_lower()