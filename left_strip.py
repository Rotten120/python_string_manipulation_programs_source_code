def left_strip(word):
    for idx, char in enumerate(word):
        if char != ' ':
            return word[idx:]
    return word

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = left_strip(word_in)
    print("Output:", word_out)
