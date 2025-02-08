"""
Declare an array of random integer numbers. 
Then, iterate through it and calculate the sum 
of the even numbers in the array
"""

numbers = [3, 4, 7, 8, 1, 6, 5, 10]


def sum_even1(array):
    sum_of_even = 0
    
    for even in array:
        if even % 2 == 0:
            sum_of_even += even
    return sum_of_even

print(sum_even1(numbers))


def sum_even2(array):
    return sum(even for even in array if even % 2 == 0)
print(sum_even2(numbers))
