def to_upper_chr(chr_inp):
    char_code_a = ord('a')
    char_code_z = ord('z')
    char_code_A = ord('A')
    char_code_inp = ord(chr_inp)
    off_set = char_code_A - char_code_a

    if char_code_a <= char_code_inp <= char_code_z:
        return chr(char_code_inp + off_set)
    return chr_inp

def to_upper_str(word):
    word_out = ""
    for char in word:
        word_out += to_upper_chr(char)
    return word_out

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = to_upper_str(word_in)
    print("Output:", word_out)
