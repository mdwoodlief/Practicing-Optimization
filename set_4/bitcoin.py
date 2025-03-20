import requests
import json
import sys

if len(sys.argv) != 2:  # catch missing arg
    sys.exit("Missing command-line argument")
try:
    x = float(sys.argv[1])
except ValueError:  # catch non number arg
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")

except requests.RequestException:
    sys.exit("Exception")
else:
    # print(json.dumps(response.json(), indent=2))

    o = response.json()

    D1 = float(o["data"].get("priceUsd"))
    output = D1 * x
    print(f"${output:,.4f}")
