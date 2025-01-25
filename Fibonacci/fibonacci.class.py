class fibonacci:
    def __init__(self, term=None):
        self.term = term if term is not None else self.get_input("Enter the term: ", "term")
        self.sequence = self.get_sequence()

    def get_input(self, term, type_input):
        while True:
            try:
                value = int(input(term))
                if value < 0:
                    print(f"{type_input.capitalize()} must be greater than zero")
                else:
                    return value
            except ValueError:
                print("Invalid input")

    def get_sequence(self):
        if self.term <= 2:
            return [] if self.term <= 0 else [0] if self.term == 1 else [0, 1]

        sequence = [0, 1]
    
        for term in range(2, self.term):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence
    
    def __str__(self):
        return f"The Fibonacci sequence up to the {self.term} {'term' if self.term == 1 else 'terms'} is {self.sequence}"

if __name__=="__main__":
    fibo = fibonacci()
    print(fibo)
        
        
        
        