import requests
import sys

try:
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=30581d693bb977df41e7a29842ff8a03848a1a5911109da574150df425340edf"

    response = requests.get(url)
    output = float(response.json()["data"]["priceUsd"])

    if len(sys.argv) < 2:

        sys.exit("Missing command-line argument")

    try:
        user_input = float(sys.argv[1])
    except ValueError:

         sys.exit("Command-line argument is not a number")

    bitcoin = user_input*output
    print(f"${bitcoin:,.4f}")

except requests.RequestException:
    sys.exit()


