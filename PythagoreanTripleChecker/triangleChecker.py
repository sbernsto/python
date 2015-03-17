# triangleChecker.PY
# This program asks the user for three inputs (each side of the triangle) and 
# produces an output of whether or not the triangle is a pythagorean triple
import sys

playAgain = True;

while playAgain == True:
    
    a = input("Please enter the short side (side a): ")
    b = input("Please enter the long side (side b): ")
    c = input("Please enter the hypotenuse: ")
    
    test = int(a)**2 + int(b)**2
    
    if test == int(c)**2:
        print("Your triangle is a pythagorean triple triangle")
    else:
        print("I'm sorry, your triangle is not a pythagorean triple triangle")
        
    temp = input("Would you like to play again? (yes or no)")
    if temp == "yes":
        playAgain = True
    else:
        playAgain = False
        print("Thanks for playing...Bye!")
        sys.exit(0)
