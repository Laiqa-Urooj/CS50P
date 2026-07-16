import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=fd7cf5d71892d2616130330b8e23c76be28fa4a6d01212297374116736b97163"

    try:
        response = requests.get(url)
        data = response.json()

        price = float(data["data"]["priceUsd"])

    except requests.RequestException:
        sys.exit("Request failed")

    cost = bitcoins * price

    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()