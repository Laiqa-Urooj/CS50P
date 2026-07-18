#in a cli argument ask user the numbre of coins he wants to buy
#if the argument is wrong valueerror and exit via sys.exit with an error output
#if correct argument convert to float
#use api to look up the price of bitcoin
#output the price for coins and return a formatted output
#steps
#receiving argument with error handling-no arg,few arg,too many arg ,wrong arg
#fetching api data in a readable way
#looking up the desired data
#calculating the price of coins
#format and display the output

import sys
import requests
import json
def main() :
    if len(sys.argv) != 2 :
        sys.exit("Missing command-line argument")   
    try :
        bitcoins = float(sys.argv[1])
    except ValueError :
        sys.exit("Command line argument is not a number")
        url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=fd7cf5d71892d2616130330b8e23c76be28fa4a6d01212297374116736b97163"  
    try :
        response = requests.get(url)
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException :
        sys.exit("Request Failed") 
        
    cost = bitcoins * price
    print(f"${price :,.4f}")
    # print(json.dumps(data,indent = 4))


if __name__ == "__main__":
    main()