#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
HARD_LEVEL_LIVES = 5
EASY_LEVEL_LIVES = 10
#end_of_game = False
from random import randint
from art import logo

#check the user's number against the actual answer
def compare_num(number_guess, chosen_number, turns_left):
  if number_guess > chosen_number: 
    print("Too High")
    return turns_left -1 
  elif number_guess < chosen_number:
    print("Too Low")
    return turns_left -1
  else:
    print(f"  You got it! The answer was {chosen_number}. ")
##################################################################################  

#making a function to set difficulty
def difficulty():
  user_level = input("Choose a diffifculty. Type 'easy' or 'hard': ")
  if user_level == 'easy': 
    return  EASY_LEVEL_LIVES
  else:
    return HARD_LEVEL_LIVES
##################################################################################
    
def game():
  print(logo)
  #make a number list and choosing a random number between 1 and 100 
  print("Welcome to Number Guessing Game")
  print("I'm thinking of number between 1 and 100. ")
  chosen_number = randint(1, 100)
  #testing code
  print(f'Pssst, the solution is {chosen_number}.')
  turns_left = difficulty()
  
  #repeating the guessing function if the user wrong
  number_guess = 0
  while number_guess != chosen_number: 
    print(f"You have {turns_left} attempts remaining to guess the number. ")
    
    #making a function called guess to guess the random number
    number_guess = int(input("Make a guess: "))

    #track the number of guesees left and reduce by -1 if they get it wrong
    turns_left = compare_num(number_guess, chosen_number, turns_left)
    if turns_left == 0:
      print("You've ran out of turns you loose! :(")
      return 
    elif number_guess != chosen_number:
      print("Guess Again.")

game()
  