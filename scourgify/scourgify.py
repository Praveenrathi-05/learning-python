import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        students = []
        
        for row in reader:
            last, first = row["name"].split(",")

            students.append({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"].strip()
            })

    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["first", "last", "house"]
        )
        writer.writeheader()
        writer.writerows(students)

except FileNotFoundError:
    sys.exit("File does not exist")
