
def count_words(text: str):
    return len(text.split())

def count_chars(text: str):
    count_table = {}
    lower_text = text.lower()
    for c in lower_text:
        #access key "c" -- init to 0 if it doesnt exist -- and add 1
        count_table[c] = count_table.get(c, 0) + 1


    return count_table

def sort_dict(dict: dict):
    dict_list = []

    for key in dict:
        new_dict = {"char": key, "count": dict[key]}
        dict_list.append(new_dict)

    def sort_on(dict):
        return dict["count"]
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

    