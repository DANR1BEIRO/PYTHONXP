"""
Tuples:
Imutable, except delete the entire tuple
can be assign without parentesis

"""

snack = "hamburger", "juice", "pizza", "flan"

for i in snack:
    print(i)
    
for i in range(0, len(snack)):
    print (snack[i])
    
for index, i in enumerate(snack, start=1):
    print(f"{index} - {i}")
    
print(sorted(snack))

x = (2, 5, 4)
y = (5, 8, 1, 2)
w = x + y
print(w)
print(w.count(5))
print(w.index(8))

name = ("goku", 39, "M", 100)
del(name)
print(name)