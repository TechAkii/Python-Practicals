# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Main program
if __name__ == "__main__":
    terms = int(input("Enter the number of terms for Fibonacci sequence: "))
    print(f"Fibonacci sequence up to {terms} terms: {fibonacci(terms)}")
