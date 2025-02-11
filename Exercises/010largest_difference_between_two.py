"""
Declare an integer array, then create a program
that calculate the largest difference between two
numbers in the array

[8, 11, 4, 1]

expected:
display 10, because the largest difference 
is 11 - 1 = 10

"""

arr = [8, 11, 4, 1]

# O(n^2)
def quadratic_time(array):
    big = 0
    for num1 in array:
        for num2 in array:
            if num1 - num2 > big:
                big = num1 - num2
    return big

print(quadratic_time(arr))

# O(n)

def linear_time(array):
    return max(array) - min(array)

print(linear_time(arr))

# more Pythonic way without using built-in functions O(n)

def linear_time2(array):
    
    min_number = max_number = array[0]
    
    # loop through the array to find the min and max number.
    for number in array:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
            
    return max_number - min_number
            
print(linear_time2(arr))

            
            
