def main():

    user_input = input("Please input a string: ").lower()
    words_count_dict = {}
    for word in user_input.split():
        if word not in words_count_dict:
            words_count_dict[word] = 1
        else:
            words_count_dict[word] += 1
    print(words_count_dict)



main()