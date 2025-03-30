def remove_suffix(word, suffix):
    suffix_len = len(suffix)
    if word[-suffix_len:] == suffix:
        return word[:-suffix_len]
    return word

if __name__ == "__main__":
    word_in = input("Input a string: ")
    suffix = input("Input suffix to remove: ")
    word_out = remove_suffix(word_in, suffix)
    print("Output:", word_out)
