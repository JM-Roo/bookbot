def get_num_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return num_words


def char_count(text):
    count_dict = {}
    lower_text = text.lower()

    for character in lower_text:
        if str(character) in count_dict:
            count_dict[str(character)] += 1
        else:
            count_dict[str(character)] =1
    
    return count_dict