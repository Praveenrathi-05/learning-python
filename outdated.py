months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "," in date:
            date = date.replace(",", "")
            month, day, year = date.split()

            month = months.index(month.title()) + 1
            day = int(day)

            if not 1 <= day <= 31:
                continue

        elif "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                continue

        else:
            continue

        print(f"{int(year):04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        continue