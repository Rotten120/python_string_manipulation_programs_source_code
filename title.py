def title(words):
    words_arr = words.split()
    words_out = words_arr[0].capitalize()
    
    for word in words_arr:
        capitalized = word.capitalize()
        if capitalized == words_out: continue
        words_out += " " + capitalized
    
    return words_out

if __name__ == "__main__":
    word_in = input("Input a string: ")
    word_out = title(word_in)
    print("Output:", word_out)
