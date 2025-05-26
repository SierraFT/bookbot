def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def character_count(book_text):
    count = {}
    for character in book_text.lower():
        if character not in count:
            count[character] = 1
        else:
            count[character] +=1
    return count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_dict = []
    for char, num in dict.items():
        sorted_dict.append({"char": char, "num": num})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict