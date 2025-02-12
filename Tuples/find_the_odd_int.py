"""
Given an array of integers, find the one that appears
an odd number of times.

There will always be only one integer that appears
an odd number of times.
"""

def find_it(seq):
    pointer = 0
    counter = {}
    counter[seq[0]] = 1
    
    while pointer < len(seq) -1:
        pointer += 1
        if counter.get(seq[pointer]):
            counter[seq[pointer]] += 1
        else:
            counter[seq[pointer]] = 1
            
    for index, value in counter.items():
        if value % 2 != 0:
            return index
            
            
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])) # -> 5
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) # -> 5
    
def find_it2(seq):
    for i in seq:
        if seq.count(i)%2==1:
            return i
        
print(find_it2([20,1,1,2,2,3,3,5,5,4,20,4,5])) # -> 5
print(find_it2([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))