# main.py
# This program writes the lyrics to 99 bottles of beer on the wall

beers = reversed(range(1,100))

for x in beers:
    if x != 1:
        print(x, "Bottles of beer on the wall", x, "Bottles of Beer, You take one down you pass it around", x-1, "Bottles of beer on the wall\n")
    
    if x == 1:
        print(x, "Bottle of beer on the wall", x, "Bottle of Beer, You take one down you pass it around", x-1, "Bottles of beer on the wall")
    

