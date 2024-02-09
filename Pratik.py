def find_odd_length_max_word(num_words, sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Filter out the words with odd length
    odd_length_words = [word for word in words if len(word) % 2 == 1]

    if not odd_length_words:
        return "Try Again"  # No odd length words found, computer response

    # Find the word with the maximum length among odd length words
    max_odd_length_word = max(odd_length_words, key=len)

    return max_odd_length_word

# Get inputs from the user
num_words = int(input("Enter the number of words in the tree: "))
sentence = input("Enter the sentence that can be composed from the tree: ")

# Call the function to find Raghu's winning word
result = find_odd_length_max_word(num_words, sentence)

# Display the result
print("Computer's response:", result)