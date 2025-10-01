import sys
from stats import get_chars_sorted_list, get_num_words
from stats import get_num_chars


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    content = get_book_text(path)
    num_words = get_num_words(content)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    chars_dict = get_num_chars(content)
    chars_list = get_chars_sorted_list(chars_dict)
    print("--------- Character Count -------")

    for i in chars_list:
        if not i["char"].isalpha():
           continue
        print(f"{i['char']}: {i['num']}")

    print("============ END ============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
main()