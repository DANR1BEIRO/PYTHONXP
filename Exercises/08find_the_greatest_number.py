"""
Create a program that declares an integer 
array and finds the greatest number in it
"""


numbers = [3, 4, 1, 8, 11, 7, 5]

def findGreater(array):
    greater = array[0]

    for number in array:
        if number > greater:
            greater = number
    return greater

print(findGreater(numbers))

