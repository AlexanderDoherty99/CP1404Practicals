def create_wordcount_dictionary_from_text(text):
    words_count_dict = {}
    for word in text.split():
        if word not in words_count_dict:
            words_count_dict[word] = 1
        else:
            words_count_dict[word] += 1
    return words_count_dict

def main():

    user_input = input("Please input a string: ").lower()
    words_count_dict = create_wordcount_dictionary_from_text(user_input)
    print(words_count_dict)



main()