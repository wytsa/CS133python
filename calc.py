# calc.py
# this prog is intended for making functions for common problems.

# mpg = (100 * lpg)/(kmpm * lp100km)
# definitions
# mpg	=	miles per gallon
# lp100km	=	liters per 100 km
# lpg	=	liters per gallon (Imperial) = 3.785411784
# kmpm	=	kilometers per mile = 1.609344 

def fuelEconomy(x):
    # x = eval(input("how many liters? "))
    lpkm = x / 100
    print("you will use about", lpkm, "l/km.")

def main():
    print()


main()
