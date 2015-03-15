# Magic8Ball.py
# This program opens with a welcome screan, asks the user for an input
# and then provides an answer from a list of 20 possibilities.

import time
import random

print("Welcome to the Magic 8-Ball!\n")

# Create list of random answers
list8Ball = ['Of Course', 'Definitely', 'The future is unclear','Yes', 'No', 'Maybe']

# Set while loop variable to True
answer = True

#While loop
while answer == True:
    print("Please think of your question: ")
    time.sleep(5)
    print("My answer is ", random.choice(list8Ball))
    
    answer = input("Do you want to ask another? (True or False)")