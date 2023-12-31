import random

word_list = ["orange" , "banana" , "apple" , "watermelon" , "grapes"]

word = random.choice(word_list)

class Hangman:
 """
 This class is used to represent the Hangman game.
 
 Attributes:
  word_list(List): Represents a list of words in the form of strings.
  num_lives(int): Represents the number of lives user has throughout the game, default is 5.
  word(str): A word chosen at random within word_list
  word_guessed(list): Represents a list of letters of a word and unguessed with underscores.
  num_letters(int): Represents the number of letters that have not been guessed yet.
  list_og_guessed(list): List of letters that have already been guessed.
  """
 
 def __init__(self, word_list, num_lives=5):
  """ 
  Intialize a Hangman game instance.
  
  Parameters:
    word_list(List): Represents a list of words in the form of strings.
  num_lives(int): Represents the number of lives user has throughout the game, default is 5.
  """
  self.word_list = word_list
  self.num_lives = num_lives
  self.word = word
  self.word_guessed = ['_'] * len(self.word)
  self.num_letters = len(set(self.word))
  self.list_of_guesses = []

 
 
 def check_guess(self, guess):
   """ 
   This function is used to check if the user's guess is within the word selected from word_list, if it is 
   it will add it the word_guessed if incorrect it will minus a life off of the 5 lives you have and also state 
   that the letter is not in the word.

   Args: guess: the user's input 
   """
  
   guess = guess.lower()
   if guess in self.word:
    print(f"Good guess! {guess} is in the word.")
    for i in range(len(self.word)):
     if self.word[i] == guess:
      self.word_guessed[i] = guess
      self.num_letters -= 1
   else:
    self.num_lives -= 1
    print(f"Sorry, {guess} is not in the word.")
    print(f"You have {self.num_lives} lives left.")


 def ask_for_input(self):
  """
  This function is used to ask the user for the input
  
  The function takes in an input and ensures that it is a valid single alphabetical character
  and also that the guess has not been guessed already if so then the code will print out stating
  either it is an invalid input or that you have tried the letter otherwise the function will check if 
  the guess is correct or incorrect and add it to the list of guesses."""
  
  while True:
   guess = input("Enter a single letter: ")
   if len(guess) != 1 or not guess.isalpha():
    print( "Invalid letter. Please, enter a single alphabetical character.")
   elif guess in self.list_of_guesses:
    print("You already tried that letter!")
   else:
    self.check_guess(guess)
    self.list_of_guesses.append(guess)
    break

    
def play_game(word_list):
  """ 
  A function used to run the Hangman game.

  Parameter:
   word_list(list): Represents a list of words for the game in the form strings
   This function starts the game with a list of words and 5 lives as its default. It then enters
   a loop where the player is asked for guessed, this continues till the user either guessed the 
   word correctly or loses their lives(5) in which case loses the game too"""
  num_lives 
  game = Hangman(word_list, num_lives)

  while True:
   if game.num_lives == 0:
    print("You lost!")
    break
   elif game.num_letters > 0:
    game.ask_for_input()
   else:
    print("Congratulations. You won the game!")
    break

play_game(word_list)
