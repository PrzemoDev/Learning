#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:     Study
#
# Author:      Przemek
#
# Created:     03-11-2016
# Copyright:   (c) Przemek 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def counter(text, letter):
    count = 0
    for loop in text:
        if loop == letter:
            count += 1
    return(count)

file = input("What's you file name?:")
file += ".txt"
with open(file) as f:
    text = f.read()
letter = input("What letter you are looking for?:")

for loop in text:
    final = 100 * counter(text, letter) / len(text)

print("Percentage of the text letter" " " + \
letter.upper() + " equals " + "%.2f" %final + "%")