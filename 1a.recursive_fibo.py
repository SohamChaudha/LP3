# Function to calculate Fibonacci number recursively
def fibonacci(n):

    # Base condition
    if n <= 1:
        return n

    # Recursive calls
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Take input from the user
n = int(input("Enter the number of terms: "))

# Print the entire Fibonacci series
print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")
