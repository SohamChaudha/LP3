# Function to generate Fibonacci series
def fibonacci(n):

    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1

    # Loop runs n times to generate n Fibonacci numbers
    for i in range(n):

        # Print the current Fibonacci number
        print(a, end=" ")

        # Calculate the next Fibonacci number
        c = a + b

        # Update a with the value of b
        a = b

        # Update b with the value of c
        b = c


# Take input from the user
n = int(input("Enter the number of terms: "))

# Call the Fibonacci function
fibonacci(n)