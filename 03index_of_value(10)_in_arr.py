"""""
Declare an array of integer numbers, then create a program that
verifies if the number 10 exists in the array. If it does, display its index;
otherwise, display -1
"""

# 1
arr = [1, 2, 3, 4, 10, -70]

for i in range(len(arr)):
    if arr[i] == 10:
        print(i)

# 2    
def findIndex(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

print(findIndex(arr, 10))

# 3
def find_index(arr, target):
    return arr.index(target) if target == 10 else -1

print(find_index(arr, 10))

