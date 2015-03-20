# coinEstimator.PY2
# Date: 17 March 2015
# Purpose: Ask user for weight of types of coins (pennies, nickles, dimes, quarters)
#           and output how many coins they have, how many wrappers they need, and how 
#           much all the coins are worth.

import math
print("Welcome To The Coin Estimator, v2.0")

coin_types = [
["pennies", 2.5, 0.01, 50],
["nickles", 5.0, 0.05, 40],
["dimes", 2.268, 0.1, 50],
["quarters", 5.67, 0.25, 40]
]


bank = 0.0

for coin, weight, value, roll in coin_types:
    weight_choice = input("Are your",coin,"weighted in g or lbs?")
    while weight_choice.lower() != "g" and weight_choice.lower() != "lbs":
        weight_choice = input("Please enter g or lbs:")
        
    coinWeight = float(input("Enter the weight of your",coin,":"))
    if weight_choice.lower == "lbs":
        coinWeight *= 453.592
        
    coinCount = math.ceil(coinWeight/weight)
    coinWrapper = math.ceil(coinCount/roll)
    print("You have approx. %s %s and you will need %s rolls." %str(coinCount), coin, str(coinWrapper))
    
    bank += (coinCount * value)
    
print("You have approx. $",bank, sep='')
