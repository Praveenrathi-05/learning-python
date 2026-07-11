def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x < 0 or y <= 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


if __name__ == "__main__":
    main()
