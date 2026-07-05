def main():
    x, op, y = input("Expression: ").split()

    x = float(x)
    y = float(y)

    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)

main()