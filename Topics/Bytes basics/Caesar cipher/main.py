if __name__ == '__main__':
    user_input = input()
    new_word = ""
    for i in user_input:
        new_word += chr(ord(i) + 1)
    print(new_word)
