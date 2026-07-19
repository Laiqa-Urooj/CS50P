def main():
    text = input("Input: ")
    output = shorten(text)
    print(output)


def shorten(word):
    vowels = "aeiouAEIOU"
    output=""
    for character in word :
        if character not in vowels :
            output += character         
    return output


if __name__ == "__main__":
    main()