def left_just(word, line_len):
    space_len = line_len - len(word)
    if space_len > 0:
        return word + (' ' * space_len)
    return word

if __name__ == "__main__":
    word_in = input("Input a string: ")
    line_len = int(input("How long does the line should be? "))
    word_out = left_just(word_in, line_len)
    print("Output:", word_out)
