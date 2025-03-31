from stats import number_of_words, character_count, list_of_dicts
import sys


def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


    
def main():
    text = get_book_text(sys.argv[1])
    number = number_of_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")

    countOfCharacters = character_count(text)
    sortedCharacters = list_of_dicts(countOfCharacters)

    for char in sortedCharacters:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")

    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()