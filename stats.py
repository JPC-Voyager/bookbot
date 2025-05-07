def count_words(text):
    # Your word counting logic here
    words = text.split()
    return len(words)

def count_characters(text):
    # Create an empty dictionary to store character counts
    chars_dict = {}

    # Loop through each character in the text
    for char in text:
        # Convert to lowercase
        lowered = char.lower()

   # If we've seen this character before, increment its count
        # Otherwise, add it to the dictionary with a count of 1
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
            
    return chars_dict

def sort_characters(char_dict):
    # Create a list to hold our dictionaries
    sorted_chars = []

    # Convert each key-value pair into a dictionary and add to the list
    for char, count in char_dict.items():
            sorted_chars.append({"char": char, "num": count})

    # Define a function to get the "num" value for sorting
    def sort_on(dict):
            return dict["num"]
    
    # Sort the list in descending order
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars