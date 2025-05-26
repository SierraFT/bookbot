import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    from stats import get_num_words, character_count, sort_dict
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    total_count = get_num_words(book_text)
    dict_count = character_count(book_text)
    sorted_count = sort_dict(dict_count)        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()


