numbers = [3, 4, 7, 8, 1, 6, 5, 10]
even_numbers = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers += num

print(even_numbers)