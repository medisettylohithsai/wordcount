def count_words(input_text):
    # Split the input text into words
    words = input_text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ")

    # Count words in the input
    word_count = count_words(user_input)

    # Display the word count
    print("Word count:", word_count)

if __name__ == "__main__":
    main()
