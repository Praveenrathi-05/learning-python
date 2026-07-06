def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 or not (s.isalnum()):
        return False
    if not s[:2].isalpha():
        return False
    is_digit = False
    is_first_zero = True
    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] != '0':
                is_first_zero = False
            if is_first_zero and s[i] == '0':
                return False
            is_digit = True
        elif s[i].isalpha() and is_digit:
            return False
    return True

main()
