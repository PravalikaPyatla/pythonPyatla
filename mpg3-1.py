#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()
repeat = 'y'
while repeat == 'y':
    # get input from the user
    miles_driven = float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))
    cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_cost = gallons_used * cost_per_gallon
        cost_per_mile = round(total_cost/miles_driven,1)
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ",total_cost)
        print("Cost Per Mile:             ",cost_per_mile)
        print()
    repeat = input("Get entries for another trip (y/n)? ")
    print()
print()
print("Bye")



