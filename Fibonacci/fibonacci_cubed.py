# lambda function to calculate the cube of a number
# (raised to the power of 3, to the power of 3 or just `cubed`)
cube = lambda x: x ** 3

# The function shouldn't ask for input inside it if it already receives the number as an argument
def fibonacci():
    while True:
        try:
            number = int(input("Fibonacci: "))
            if number >= 0:
                break
            else:
                print("Number must be greater than 0!")
        except ValueError:
            print("Only integer numbers are allowed!")

    if number <= 2:
        return [] if number <= 0 else [0] if number == 1 else [0, 1]
    sequence = [0, 1] # starts with 0, 1
    for x in range(2, number): # calculates from 2 up the desired position
        next_value = sequence[-1] + sequence[-2] # adds the last two number of the sequence
        sequence.append(next_value) # adds the sum of the last two numbers to the end of the list
        
    return sequence

if __name__=="__main__":
    result = fibonacci()
    fibonacci_cubed = list(map(cube, result))
    print(f"The fibonacci sequence cubed is {fibonacci_cubed}")

