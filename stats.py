# This file is for book statistics

def word_counter(book_text):
    book_words = book_text.split()
    word_count = len(book_words)
    return word_count

def character_counter(book_text):
    lower_book_text = book_text.lower()


    letters_only = []

    for letters in lower_book_text:
        if letters.isalpha():
            letters_only.append(letters)

    character_counts = {}

    for character in letters_only:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts

def sorting(character_dictionary):
    # Convert dict to list of (key, value) pairs
    items_list = list(character_dictionary.items())

    # Sort in place using .sort()
    def get_value(item):
        return item[1]

    items_list.sort(key=get_value, reverse=True)

    # Convert back to a dict
    sorted_dict = dict(items_list)
    return sorted_dict