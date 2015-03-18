# coinEstimator.PY2
# Date: 17 March 2015
# Purpose: Ask user for weight of types of coins (pennies, nickles, dimes, quarters)
#           and output how many coins they have, how many wrappers they need, and how 
#           much all the coins are worth.

#Weights of each coin (grams)
pennyWeight = 2.5
nickleWeight = 5
dimeWeight = 2.268
quarterWeight = 5.67

#Number of coins in each wrapper
pennyWrapper = 50
nickleWrapper = 40
dimeWrapper = 50
QuarterWrapper = 40

#Welcome Screen
print("Welcome To The Coin Estimator")

# User input
pennies = input("What is the weight of your pennies?:")
nickles = input("What is the weight of your nickles?")
dimes = input("What is the weight of your dimes?: ")
quarters = input("What is the weight of your quarters?:")

#Convert input strings to floating point numbers
pennies = float(pennies)
nickles = float(nickles)
dimes = float(dimes)
quarters = float(quarters)

#Calculate how many coins you have
numPennies = pennies/pennyWeight
numNickles = nickles/nickleWeight
numDimes = dimes/dimeWeight
numQuarters = quarters/quarterWeight

# Print out how many of each coin you have
print("You have the following coins:")
print("Pennies:",int(numPennies))
print("Nickles: ",int(numNickles))
print("Dimes: ",int(numDimes))
print("Quarters: ", int(numQuarters))

#Determine and print the number of wrappers needed

#Print out the total value of all the coins
totalValue = numPennies*0.01 + numNickles*0.05 + numDimes*0.1 + numQuarters*0.25
print("The total value of your coins is: $", round(totalValue,2))



