def fibonacci():
    """
    A function that takes a number as input and displays
    the Fibonacci sequence up to that number
    """
    while True:
        try: 
            term = int(input("Fibonacci term: "))
            if term <= 0:
                print("Term must be greater than zero!")
            else:
                break
        except ValueError:
            print("Term must be a integer number!")
            
    if term <= 2:
        return [] if term <= 0 else [0] if term == 1 else [0, 1]

    sequence = [0, 1]
    
    for x in range(2, term):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence
        
if __name__=="__main__":
    result = fibonacci()
    print(f"The fibonacci sequence up to {len(result)} terms is: {result}")

