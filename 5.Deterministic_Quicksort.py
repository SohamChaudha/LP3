# Function to partition the array using a fixed pivot
def partition(arr, low, high):

    # Select the last element as the pivot
    pivot = arr[high]

    # i represents the position of smaller elements
    i = low - 1

    # Traverse the array from low to high-1
    for j in range(low, high):

        # Check if the current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # Move the smaller element position forward
            i = i + 1

            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the final position of the pivot
    return i + 1


# Function to perform Deterministic Quick Sort
def quick_sort(arr, low, high):

    # Check whether the array contains more than one element
    if low < high:

        # Partition the array and get the pivot position
        pi = partition(arr, low, high)

        # Recursively sort the left part of the pivot
        quick_sort(arr, low, pi - 1)

        # Recursively sort the right part of the pivot
        quick_sort(arr, pi + 1, high)


# Main program

# Take array elements from the user
arr = list(map(int, input("Enter array elements: ").split()))

# Call Quick Sort function
quick_sort(arr, 0, len(arr) - 1)

# Display the sorted array
print("Sorted Array:", arr)