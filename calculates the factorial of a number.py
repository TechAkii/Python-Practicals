# Factorial using Iterative Method
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial using Recursive Method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Main program to test both methods
if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))
    
    print(f"Factorial of {number} (Iterative): {factorial_iterative(number)}")
    print(f"Factorial of {number} (Recursive): {factorial_recursive(number)}")
