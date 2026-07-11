def shorten(word):
    vowels = "aeiou"
    return "".join(c for c in word if c.lower() not in vowels)


def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


if __name__ == "__main__":
    main()
