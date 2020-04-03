def create_wordcount_dictionary_from_text(text):
    words_count_dict = {}
    for word in text.split():
        if word not in words_count_dict:
            words_count_dict[word] = 1
        else:
            words_count_dict[word] += 1
    return words_count_dict


def output_dict_keys_and_values(words_count_dict):
    longest_key = 0
    for key in sorted(words_count_dict.keys()):
        if len(key) > longest_key:
            longest_key = len(key)
    for key in sorted(words_count_dict.keys()):
        print("{:{}} : {}".format(key, longest_key, words_count_dict[key]))


def main():

    user_input = input("Please input a string: ").lower()
    words_count_dict = create_wordcount_dictionary_from_text(user_input)
    output_dict_keys_and_values(words_count_dict)


main()