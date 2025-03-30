import math

def center(word, line_len):
    space_len = (line_len - len(word)) / 2
    left_space = ' ' * math.floor(space_len)
    right_space = ' ' * math.ceil(space_len)
    if space_len > 0:
        return (left_space + word + right_space)
    return word

if __name__ == "__main__":
    word_in = input("Input a string: ")
    line_len = int(input("How long does the line should be? "))
    word_out = center(word_in, line_len)
    print("Output:", word_out)
    
