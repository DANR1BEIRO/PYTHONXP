"""
Declare an array of random numbers, then iterate through it,
filtering only the even numbers and storing them in a new array.
After that, display the array containing only the even numbers
"""
numbers = [1, 4, 12, 21, 53, 88, 112]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        
print(even_numbers)