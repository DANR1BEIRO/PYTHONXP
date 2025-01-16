def fibonacci():
    """
    Generate a Fibonacci sequence up to the user specified term
    """
    while True:
        try:
            term = int(input("Enter fibo term: "))
            if 0 < term:
                break
            else:
                print("Term must be greater than zero")
        except ValueError:
            print("Term must be an integer number")

    if term <= 2:
        return [0] if term == 1 else [0,1]

    sequence = [0,1]
    for i in range(2, term):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

if __name__=="__main__":
    fibo = fibonacci()
    print(f"The fibonacci sequence up to {len(fibo)} {'term' if len(fibo) == 1 else 'terms'} is {fibo}")