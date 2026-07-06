text = input("Input: ")
vowels = "aeiou"
short_str = "Output: "
for char in text:
    if char.lower() not in vowels:
        short_str += char
print(short_str)
