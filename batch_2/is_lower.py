def is_lower(word):
    char_code_A = ord('A')
    char_code_Z = ord('Z')
    is_all_lower = True

    for char in word:
        if char_code_A <= ord(char) <= char_code_Z:
            return False
    return is_all_lower

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = is_lower(word_in)
    print("Output:", word_out)
