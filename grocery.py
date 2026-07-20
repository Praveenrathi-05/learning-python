fruits = {}
while True:
    try:
        fruit = input().upper().strip()
        if fruit in fruits:
            fruits[fruit] += 1
        else:
            fruits[fruit] = 1
    except EOFError:
        break

for key, value in sorted(fruits.items()):
    print(value, key)
