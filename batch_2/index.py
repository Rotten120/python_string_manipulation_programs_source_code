def index(word, sub_str):
    idx = 0

    sub_str_len = len(sub_str)
    word_len = len(word)

    while(sub_str_len + idx <= word_len):
        if word[idx:sub_str_len + idx] == sub_str:
            return idx
        idx += 1
    return -1

if __name__ == "__main__":
    word_in = input("Input a string: ")
    sub_str = input("Input string to find: ")
    word_out = index(word_in, sub_str)
    print("Output:", word_out)
