word = input("camelCase: ").strip()
for char in word:
    if char.isupper():
        print(f"_{char.lower()}",end = "")
    else:
        print(char, end = "")
print()