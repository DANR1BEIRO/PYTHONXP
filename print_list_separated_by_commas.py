"""
Prints the elements of the list separated by commas, and the last element
ends with a period
"""
my_list = [1, 2, 3, 4, "dog", "shark", "apple"]

# Using join method (the simplest and most pythonic way):
result_join = "Using join method:\n" + ", ".join(map(str, my_list)) + ".\n"
print(result_join)

"""
map(str, my_list): Converts all elements of the list 
to strings(because join works with strings)

map() function:
The map() function applies a given function to each 
item in an iterable (like a list, tuple, etc.)
and returns a new iterable (a map object)

syntax: map(function, iterable)

str function:
str() function converts its argument into a string representation
"""

# Using for loop with indexes:
result_for_loop = "Using a for loop with indexes:\n"
for i in range(len(my_list)):
    if i < len(my_list) - 1: # If it's not the last element
        result_for_loop += str(my_list[i]) + ", "
    else:                    # If it's the last element       
        result_for_loop += str(my_list[i]) + "."
print(result_for_loop)

for i in range(len(my_list)):
    if i < len(my_list) - 1:
        print(my_list[i], end=", ")
    else:
        print(my_list[i], end=".\n")
        
"""
Loop through the list using indexes to determine
whether an element is the last one

range(len(my_list)): Iterates over the indexes of the list

if i < len(my_list) - 1: Checks if the current index isn't the last one"""

# Using Enumerate:
result_enumerate = "\nUsing enumerate:\n"
for i, n in enumerate(my_list):
    if i < len(my_list) - 1:
        result_enumerate += str(n) + ", "
    else:
        result_enumerate += str(n) + "."
print(result_enumerate)

for i, n in enumerate(my_list):
    if i < len(my_list) - 1:
        print(n, end=", ")
    else:
        print(n, end=".\n")

"""
The enumerate() function gives both the index and the value while iterating

for i, n in enumerate(my_list): Gives both the index (i) and the value (n)
of each element in the list
"""
        
# Using Slicing:

result_slicing = "\nUsing slicing:\n" + ", ".join(map(str, my_list[:-1])) + f", {my_list[-1]}."
print(result_slicing)

print(", ".join(map(str, my_list[:-1])) + f", {my_list[-1]}.")

"""
Using slicing for all but the last element you can handle
all the elements except the last one separately, then print
the last element with a period

my_list[:-1]: Slices the list to get all elements except the last one

my_list[-1]: Refers to the last element of the list

combine the two parts with the desired formatting
"""
