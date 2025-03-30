def is_upper(word):
    char_code_a = ord('a')
    char_code_z = ord('z')
    is_all_upper = True
    for char in word:
        if char_code_a <= ord(char) <= char_code_z:
            return False
    return is_all_upper
    

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = is_upper(word_in)
    print("Output:", word_out)
