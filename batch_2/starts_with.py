def starts_with(word, prefix):
    prefix_len = len(prefix)
    return (word[:prefix_len] == prefix)

if __name__ == "__main__":
    word_in = input("Input a string: ")
    prefix = input("Input a prefix: ")
    word_out = starts_with(word_in, prefix)
    print("Output:", word_out)
