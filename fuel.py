while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or x > y:
            continue

        percentage = round((x / y) * 100)
        break

    except (ValueError, ZeroDivisionError):
        continue

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")