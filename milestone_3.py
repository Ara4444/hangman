import random

word_list = ["orange" , "banana" , "apple" , "watermelon" , "grapes"]
""" 
Created a list containing 5 strings representing different fruits
"""
word =  random.choice(word_list)

def check_guess(guess):
   """ 
   This function is used to check if the user's guess is within the word selected from word_list.

   Args: guess: the user's input 
   """

   if guess in word:
     print(f"Good guess! {guess} is in the word.")
   else:
    print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
  """ 
  This function is used to ask the user for a valid input.
  
  The purpose of this function is to ensure the user inputs a single alphabetical value
  if not then the code will prompt the user saying it is invalid.
  """
  while True:
   guess = input("Enter a single letter: ")

   if len(guess) == 1 and guess.isalpha():
    print(guess, "Good Guess")
   else:
    print("Invalid letter. Please, enter a single alphabetical character.")
  check_guess(guess)



ask_for_input()


