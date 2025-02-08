"""
Declare an array with some random names. Then, create a new array
from the first one that contains only the names starting with the letters
'A' or 'a' (uppercase or lowercase). Finally, print the variable that
holds the array.
"""

names = ["Ana", "Joana", "Carlos", "amanda"]

def find_A(array):
    names_a = []
    for name in array:
        if name.startswith("A") or name.startswith("a"):
            names_a.append(name)

    return names_a

print(find_A(names))


def find_A2(array):
    names_a2 = []
    for name in array:
        if name[0] == "A" or name[0] == "a":
            names_a2.append(name)
    return names_a2

print(find_A2(names))


def find_A3(array):
    return [name for name in array if name.lower().startswith("a")]

print(find_A3(names))
            