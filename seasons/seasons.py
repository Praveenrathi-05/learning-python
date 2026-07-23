from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth = input("Date of Birth: ")

    try:
        birth_date = validate_date(birth)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_to_words(birth_date))


def validate_date(s):
    return date.fromisoformat(s)


def minutes_to_words(birth_date):
    minutes = (date.today() - birth_date).days * 1440

    return (
    p.number_to_words(minutes, andword="")
    .capitalize()
    + " minutes"
    )


if __name__ == "__main__":
    main()
