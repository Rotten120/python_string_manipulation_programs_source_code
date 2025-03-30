def ends_with(word, suffix):
    suffix_len = len(suffix)
    return (word[-suffix_len:] == suffix)

if __name__ == "__main__":
    word_in = input("Input a string: ")
    suffix = input("Input a suffix: ")
    word_out = ends_with(word_in, suffix)
    print("Output:", word_out)
