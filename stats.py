def get_num_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return num_words


def char_count_dict(text):
    count_dict = {}
    lower_text = text.lower()

    for character in lower_text:
        if str(character) in count_dict:
            count_dict[str(character)] += 1
        else:
            count_dict[str(character)] =1
    
    return count_dict

def sort_on(item):
    return item["num"]

def sorted_dict_list(input_dict):
    output_list = []
    for character in input_dict:
        if character.isalpha() == True:
            temp_dict = {}
            temp_dict["char"] = character
            temp_dict["num"] = input_dict[character]
            output_list.append(temp_dict)
        
    output_list.sort(reverse=True, key=sort_on)
    return output_list