from stats import get_num_words, char_count

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    character_count = char_count(text)
    print(character_count)


main()