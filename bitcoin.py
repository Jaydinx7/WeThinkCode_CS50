import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    responce = requests.get("https://rest.coincap.io/v3/assets?apiKey=309b5aa86b7899b44a0a83540533221403a334b717003d68d6d58949362345c6")
    x = responce.json()

    for crypto in x["data"]:
        if crypto['id'] == "bitcoin":
            usd = float(crypto["priceUsd"])
            price = usd * amount
            print(f"${price:,.4f}")
            break



except requests.RequestException:
    sys.exit()
