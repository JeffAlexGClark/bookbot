import sys
from stats import word_counter
from stats import character_counter
from stats import sorting

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text_string = get_book_text(book_path)
    number_of_words = word_counter(book_text_string)
    number_of_characters = character_counter(book_text_string)
    sorted_list = sorting(number_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_list.items():
        print(f"{char}: {count}")

    print("============= END ===============")
main()