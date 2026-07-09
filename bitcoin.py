import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=70030acc5baaa57b3aa0663b4e815adf715d0ea1af4bb18312cf02737beeb3fb"
    )
    result = response.json()

    price = n * float(result["data"]["priceUsd"])
    print(f"${price:,.4f}")

except requests.RequestException:
    pass
