import random 

word_list = ["orange" , "banana" , "apple" , "watermelon" , "grapes"]
""" 
Created a list containing 5 strings representing different fruits
"""
word =  random.choice(word_list)
print(word)
""" 
A variable named word to select a random string from word_list
"""
guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
  print(guess, "Good Guess")
else:
 print("Oops!, That is not a valid input.")
 """ 
 An input created to take in a user_input of a single letter followed by an if - 
 statement making sure the length of the user input is 1 and that it is an alphabet,
 also an else statement in the case of an invalid input and then informing the user 
 that the input is invalid
"""

 
