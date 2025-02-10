"""
Create a program that will generate five random numbers and 
store them in a tuple. After that, display the list of 
generated numbers and also indicate 
the smallest and the largest values in the tuple.
"""
from random import randint

class Random:
    def __init__(self):
        self.random = self.random_numbers()
        
    def random_numbers(self):
        numbers = []
        for _ in range(5):
            number = randint(1, 10)
            numbers.append(number)
        return tuple(numbers)
    
    def display_result(self):
        print(f"The random tuple is {self.random}")
        print(f"The greater number is {max(self.random)}")
        print(f"The smaller number is {min(self.random)}")
        
random = Random()
random.display_result()