from stats import count_words, count_chars, sort_dict

def get_book_text(path):

    with open(path) as f:
        return f.read()
    

def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    

    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")

    print("============= END ===============")


def main():

    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    text_chars = count_chars(book_text)
    sorted_list = sort_dict(text_chars)
    
    print_report(book_path, word_count, sorted_list)



main()