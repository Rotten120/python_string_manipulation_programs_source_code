def to_lower_chr(chr_inp):
    char_code_A = ord('A')
    char_code_Z = ord('Z')
    char_code_a = ord('a')
    char_code_inp = ord(chr_inp)
    off_set = char_code_A - ord('a')

    if char_code_A <= char_code_inp <= char_code_Z:
        return chr(char_code_inp - off_set)
    return chr_inp

def to_lower_str(word):
    word_out = ""
    for char in word:
        word_out += to_lower_chr(char)
    return word_out

    

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = to_lower_str(word_in)
    print("Output:", word_out)
