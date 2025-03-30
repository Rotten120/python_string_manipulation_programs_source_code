def remove_prefix(word, prefix):
    prefix_len = len(prefix)
    if word[:prefix_len] == prefix:
        return word[prefix_len:]
    return word
    

if __name__ == "__main__":
    word_in = input("Input a string: ")
    prefix = input("Input prefix to remove: ")
    word_out = remove_prefix(word_in, prefix)
    print("Output:", word_out)
