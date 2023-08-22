import random

word_list = ["orange" , "banana" , "apple" , "watermelon" , "grapes"]

word =  random.choice(word_list)

class Hangman():
 def __init__(self,word_list, num_lives = 5):
  self.word_list = word_list
  self.num_lives = num_lives
  self.word = random.choice(word_list)
  self.word_guessed = ['_' for _ in self.word]
  self.num_letters = len(set(self.word))
  self.list_of_guesses = []

 
 def check_guess(self, guess):
  guess = guess.lower()
  
  if guess in self.word:
   print(f"Good guess! {guess} is in the word.")
   for i, letter in enumerate(self.word):
    if letter == guess:
     self.word_guessed[i] = guess
    self.num_letters -= 1
    print("Word guessed so far:", ' '.join(self.word_guessed))
  else:
     num_lives -= 1
     print(f"Sorry, {letter} is not in the word. Try again.")
     print(f"You have {num_lives} lives left.")


 def ask_for_input(self):
  while True:
   guess = input("Enter a single letter: ")
   if len(guess) != 1 or not guess.isalpha():
    print( "Invalid letter. Please, enter a single alphabetical character.")
   elif guess in self.list_of_guesses:
    print("You already tried that letter!")
   else:
    self.check_guess(guess)
    self.list_of_guesses.append(guess)

