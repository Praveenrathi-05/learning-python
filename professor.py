import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        wrong = 0
        x , y = generate_integer(level) , generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
            except ValueError:
                pass

            print("EEE")
            wrong += 1

            if wrong == 3:
                print(f"{x} + {y} = {x+y}")
                break
            
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
