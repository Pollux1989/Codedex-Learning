print("#####--------20. Planets Weights--------#####")

''' 
The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

Asks the user what their Earth weight is (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight * relative gravity

Number	Planet	    Relative Gravity
1	    Mercury	    0.38
2	    Venus	    0.91
3	    Mars	    0.38
4	    Jupiter	    2.53
5	    Saturn	    1.07
6	    Uranus	    0.89
7	    Neptune	    1.14

If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

'''
earth_weight = float(input("What is your the Earth Weight:  "))
print("1 - Mercury")
print("2 - Venus")
print("3 - Mars")
print("4 - Jupiter")
print("5 - Saturn")
print("6 - Uranus")
print("7 - Neptune")
planet_choise = int(input('Which planet are you going: '))

if planet_choise == 1:
    print (earth_weight * 0.38)
elif planet_choise == 2:
    print (earth_weight * 0.91)
elif planet_choise == 3:
    print (earth_weight * 0.38)
elif planet_choise == 4:
    print (earth_weight * 2.53)
elif planet_choise == 5:
    print (earth_weight * 1.07)
elif planet_choise == 6:
    print (earth_weight * 0.89)
elif planet_choise == 7:
    print (earth_weight * 1.14)
else:
    print ('wrong planet')
