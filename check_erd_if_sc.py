import requests
import logging
import csv
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

RATE_LIMIT = 2  # Number of requests per second
DELAY = 1 / RATE_LIMIT  # Delay between requests to respect rate limit

def is_not_smart_contract(address):
    """
    Checks if a given address is not a smart contract.

    Args:
        address (str): The address to check.

    Returns:
        bool: True if the address is not a smart contract, False otherwise.
    """
    url = f"https://api.elrond.com/accounts/{address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "ownerAddress" not in data and "assets" not in data and "code" not in data:
            return True
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed for address {address}: {e}")
    return False

def filter_smart_contracts(input_filename, output_filename):
    """
    Filters out smart contract addresses from the CSV file.

    Args:
        input_filename (str): The name of the input CSV file.
        output_filename (str): The name of the output CSV file.
    """
    with open(input_filename, mode='r') as infile, open(output_filename, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['address', 'balance'])
        
        for row in reader:
            address = row['address']
            balance = row['balance']
            if is_not_smart_contract(address):
                writer.writerow([address, balance])
            time.sleep(DELAY)  # Respect the rate limit
        logging.info(f"Filtered holders saved to {output_filename}")

if __name__ == "__main__":
    filter_smart_contracts('holders.csv', 'filtered_holders.csv')
