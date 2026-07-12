import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1]) as file:
                total = 0
                for line in file:
                    if not (line.strip().startswith("#") or line.strip() == ""):
                        total += 1
                print(total)
        except FileNotFoundError:
            sys.exit("File does not exist")
