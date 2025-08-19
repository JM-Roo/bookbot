import sys
from stats import get_num_words, char_count_dict, sorted_dict_list

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    character_count_dict = char_count_dict(text)
    sorted_dict = sorted_dict_list(character_count_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_dict)):
        print(f"{sorted_dict[i]["char"]}: {sorted_dict[i]["num"]}")
    print("============= END ===============")


main()