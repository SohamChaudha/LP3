# Import random module to select a random pivot
import random


# Function to partition the array
def partition(arr, low, high):

    # Select the last element as pivot
    pivot = arr[high]

    # Initialize the boundary of smaller elements
    i = low - 1

    # Traverse the array except the pivot
    for j in range(low, high):

        # Check if current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # Move the boundary forward
            i = i + 1

            # Swap the elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return pivot position
    return i + 1


# Function to select a random pivot
def randomized_partition(arr, low, high):

    # Generate a random index between low and high
    random_index = random.randint(low, high)

    # Swap the randomly selected element with the last element
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Perform normal partitioning
    return partition(arr, low, high)


# Function to perform Randomized Quick Sort
def randomized_quick_sort(arr, low, high):

    # Check whether the array contains more than one element
    if low < high:

        # Partition using a randomly selected pivot
        pi = randomized_partition(arr, low, high)

        # Recursively sort the left partition
        randomized_quick_sort(arr, low, pi - 1)

        # Recursively sort the right partition
        randomized_quick_sort(arr, pi + 1, high)


# Main program

# Take array elements from the user
arr = list(map(int, input("Enter array elements: ").split()))

# Call Randomized Quick Sort
randomized_quick_sort(arr, 0, len(arr) - 1)

# Display sorted array
print("Sorted Array:", arr)     