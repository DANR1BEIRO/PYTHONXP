# lambda function to calculate the cube of a number
# (raised to the power of 3, to the power of 3 or just `cubed`)
cube = lambda x: x ** 3

# The function shouldn't ask for input inside it if it already receives the number as an argument
def fibonacci():
    """
    Generate a Fibonacci sequence up to the user specified term
    """
    while True:
        try:
            term = int(input("Fibonacci: "))
            if 0 < term:
                break
            else:
                print("Number must be greater than 0!")
        except ValueError:
            print("Only integer numbers are allowed!")

    if term <= 2:
        return [0] if term == 1 else [0,1]
    
    sequence = [0, 1] # starts with 0, 1
    for x in range(2, term): # calculates from 2 up the desired position
        next_value = sequence[-1] + sequence[-2] # adds the last two number of the sequence
        sequence.append(next_value) # adds the sum of the last two numbers to the end of the list     
    return sequence

if __name__=="__main__":
    fibo = fibonacci()
    fibonacci_cubed = list(map(cube, fibo))
    print(f"The cubed fibonacci sequence up to {len(fibo)} {'term' if len(fibo) == 1 else 'terms'} is {fibonacci_cubed}")

