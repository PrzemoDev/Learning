#-------------------------------------------------------------------------------
# Name:        Making Functions - Student's Average
# Purpose:     Study
#
# Created:     17-10-2016
# Copyright:   (c) PrzemoDev
#-------------------------------------------------------------------------------

#This bit of code simply gives us average of whole class.


def average_overall(nmb):   #"nmb" must be a list.
    total = sum(nmb)
    return total / len(nmb)


#This lines calculates
#one students average
#per run.
def average_of_student(student):
    tests = average_overall(student["tests"])
    short_tests = average_overall(student["short_tests"])
    total  = tests * 0.6 + short_tests * 0.4
    return total

def average_of_class(students):
    total = []  #It must be a list!
    for loop in students:
        total.append(average_of_student(loop))
    total_overall = average_overall(total)
    print("Average of class equals %.2f" % total_overall)


przemek = {
    "name": "Przemek",
    "tests": [5, 5 ,5],
    "short_tests": [5, 4 ,5]
    }

magda = {
    "name": "Magda",
    "tests": [5, 5 ,5],
    "short_tests": [5, 5 ,5]
    }

ClassB1 = [przemek, magda]
average_of_class(ClassB1)

