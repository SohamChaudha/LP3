# Function to solve 0/1 Knapsack
def knapsack(weights, profits, capacity):

    # Find the number of items
    n = len(weights)

    # Create a DP table with (n+1) rows and (capacity+1) columns
    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    # Traverse through all items
    for i in range(1, n + 1):

        # Check every possible capacity
        for j in range(capacity + 1):

            # If item weight is greater than current capacity
            if weights[i - 1] > j:

                # We cannot include the item
                dp[i][j] = dp[i - 1][j]

            else:

                # Option 1: Exclude the current item
                exclude = dp[i - 1][j]

                # Option 2: Include the current item
                include = profits[i - 1] + dp[i - 1][j - weights[i - 1]]

                # Store the maximum profit
                dp[i][j] = max(include, exclude)

    # Print the DP table
    print("DP Table:")

    for row in dp:
        print(row)

    # The last cell contains maximum profit
    print("\nMaximum Profit:", dp[n][capacity])

    # Backtrack to identify selected items
    selected = []
    j = capacity

    for i in range(n, 0, -1):

        # If current value differs from previous row
        if dp[i][j] != dp[i - 1][j]:

            # Store the selected item number
            selected.append(i)

            # Reduce the remaining capacity
            j = j - weights[i - 1]

    # Display selected items
    selected.reverse()

    print("Selected Items:", selected)


# Main program

# Weight of each item
weights = [1, 2, 3, 4]

# Profit of each item
profits = [2, 3, 4, 5]

# Maximum capacity of knapsack
capacity = 5

# Call the function
knapsack(weights, profits, capacity)