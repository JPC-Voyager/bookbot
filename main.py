from stats import count_words, count_characters, sort_characters
import sys 
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath):
    # use the 'filepath' that's passed as an argument
    with open(filepath) as f:
        # read and return the file contents
        return f.read()

def main():
    # Path to the book 
    book_path = sys.argv[1]
    
    
    # Get the book text
    book_text = get_book_text(book_path)
    
    # Count words and characters
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    
    # Sort the characters by frequency
    sorted_chars = sort_characters(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each alphabetical character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()