# Import required modules
import heapq
from collections import Counter
from itertools import count


# Function to generate Huffman codes
def huffman_encoding(text):

    # Step 1: Calculate frequency of each character
    frequency = Counter(text)

    # Step 2: Create an empty min heap
    heap = []

    # Used to uniquely identify heap entries when frequencies are equal
    unique_id = count()

    # Step 3: Insert each character into the min heap
    for char, freq in frequency.items():

        # Each heap entry contains frequency, unique ID and character
        heapq.heappush(heap, (freq, next(unique_id), char))

    # Step 4: Build the Huffman Tree
    while len(heap) > 1:

        # Extract the two nodes with minimum frequencies
        freq1, id1, left = heapq.heappop(heap)
        freq2, id2, right = heapq.heappop(heap)

        # Create a new internal node with combined frequency
        merged = (left, right)

        # Insert the new node back into the min heap
        heapq.heappush(
            heap,
            (freq1 + freq2, next(unique_id), merged)
        )

    # Step 5: Generate codes by traversing the Huffman Tree
    codes = {}

    # Function to traverse the tree
    def generate_codes(node, code=""):

        # Check whether the node is a leaf node
        if isinstance(node, str):

            # Assign the generated binary code to the character
            codes[node] = code if code else "0"

            return

        # Traverse left child and append 0
        generate_codes(node[0], code + "0")

        # Traverse right child and append 1
        generate_codes(node[1], code + "1")

    # Get the root node of the Huffman Tree
    root = heap[0][2]

    # Generate Huffman codes
    generate_codes(root)

    # Step 6: Encode the original text
    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    # Display character frequencies and Huffman codes
    print("Character  Frequency  Huffman Code")

    for char, freq in frequency.items():
        print(char, "          ", freq, "         ", codes[char])

    # Display encoded message
    print("\nEncoded Message:", encoded_text)

    # Return the generated codes and encoded message
    return codes, encoded_text


# Main program
text = input("Enter the text to encode: ")

# Call the Huffman Encoding function
huffman_encoding(text)