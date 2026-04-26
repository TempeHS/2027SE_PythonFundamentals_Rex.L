def main():
    user_input = input("Enter a string: ")
    print(shorten(user_input))


def shorten(word):
    omitted_letters = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""
    for _ in word:
        if _ not in omitted_letters:
            result += _
    return result


if __name__ == "__main__":
    main()
      
      
