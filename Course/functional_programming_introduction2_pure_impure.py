#-------------------------------------------------------------------------------
# Name:        Functional Programming 2 - Pure/Impure
# Purpose:     Study
#
# Created:     03-11-2016
# Copyright:   (c) PrzemoDev
#-------------------------------------------------------------------------------

def pure_function(x, y):  #This function do not need "outside" variables.
    temp = x + 2*y
    return(temp / (2*x + y))

print(pure_function(5,7))

def impure(arg):
    some_list.append(arg)
    print(some_list)

impure(11)