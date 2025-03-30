def zero_fill(number, line_len):
    zero_len = line_len - len(number)
    if zero_len > 0:
        return ('0' * zero_len) + number
    return number

if __name__ == "__main__":
    number_in = input("Input a number: ")
    line_len = int(input("How many digits the number should be? "))
    number_out = zero_fill(number_in, line_len)
    print("Output:", number_out)
