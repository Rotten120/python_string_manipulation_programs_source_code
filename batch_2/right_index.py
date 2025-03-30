def right_index(word, sub_str):
    idx = len(word)

    sub_str_len = len(sub_str)
    word_len = len(word)

    while(idx - sub_str_len > 0):
        if word[idx - sub_str_len:idx] == sub_str:
            return idx - sub_str_len
        idx -= 1
    return -1

if __name__ == "__main__":
    word_in = input("Input a string: ")
    sub_str = input("Input string to find: ")
    word_out = right_index(word_in, sub_str)
    print("Output:", word_out)
