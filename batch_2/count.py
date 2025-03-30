def count(word, sub_str):
    sub_str_count = 0
    idx = 0
    
    sub_str_len = len(sub_str)
    word_len = len(word)

    if sub_str_len > word_len:
        return 0
    
    while(sub_str_len + idx <= word_len):
        if word[idx:sub_str_len + idx] == sub_str:
            sub_str_count += 1
            idx += sub_str_len
        idx += 1
    return sub_str_count
            

if __name__ == "__main__":
    word_in = input("Input a string: ")
    sub_str = input("Input string to count: ")
    word_out = count(word_in, sub_str)
    print("Output:", word_out)
