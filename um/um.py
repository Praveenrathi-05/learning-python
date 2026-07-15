import re

def main():
    print(count(input("Text: ")))


def count(s):
    r = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(r)

if __name__ == "__main__":
    main()
