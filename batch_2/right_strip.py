def right_strip(word):
    word_len = len(word)
    for idx in range(word_len - 1, 0, -1):
        if word[idx] == ' ':
            return word[:idx]
    return word

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = right_strip(word_in)
    print("Output:", word_out)
