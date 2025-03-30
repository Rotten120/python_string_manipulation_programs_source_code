def swap_case(word):
    char_code_A = ord('A')
    char_code_Z = ord('Z')
    char_code_a = ord('a')
    char_code_z = ord('z')
    off_set = ord('A') - ord('a')
    word_out = ""

    for char in word:
        char_code_inp = ord(char)
        if char_code_A <= char_code_inp <= char_code_Z:
            word_out += chr(char_code_inp - off_set)
        elif char_code_a <= char_code_inp <= char_code_z:
            word_out += chr(char_code_inp + off_set)
        else:
            word_out += char
            
    return word_out

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = swap_case(word_in)
    print("Output:", word_out)
