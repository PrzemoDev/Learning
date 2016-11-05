#-------------------------------------------------------------------------------
# Name:        Functional Programming
# Purpose:     Study
#
# Created:     03-11-2016
# Copyright:   (c) PrzemoDev 2016
#-------------------------------------------------------------------------------

def take_twice(a, b):     # "a" become add_five and "b" equals 10
    return(a(a(b)))       # add_five(add_five(10)) ==> 10+5=15
                          #                            15+5=20
def add_five(x):
    return(x+5)

print(take_twice(add_five,10))
