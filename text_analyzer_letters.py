#-------------------------------------------------------------------------------
# Name:        Text analyzer
# Purpose:     Study
#
# Created:     03-11-2016
# Copyright:   (c) PrzemoDev 2016
#-------------------------------------------------------------------------------

# How it works: You need to set file (in .txt) and letter you want to find.

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
letter = input("What letter are you looking for?:")

for loop in text:
    final = 100 * counter(text, letter) / len(text)

#This line is too long, but still working ^^

print("Percentage of the text letter" " " + \
letter.upper() + " equals " + "%.2f" %final + "%")

