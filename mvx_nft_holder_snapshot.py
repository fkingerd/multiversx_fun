import requests
import logging
import csv

# Configure logging
logging.basicConfig(level=logging.INFO)

RATE_LIMIT = 2  # Number of requests per second

def get_holders(collection_id):
    """
    Fetches all holders for a specific NFT collection from the API.

    Args:
        collection_id (str): The ID of the NFT collection.

    Returns:
        dict: A dictionary of holders with addresses as keys and balances as values.
    """
    base_url = f'https://api.elrond.com/collections/{collection_id}/accounts'
    holders = {}
    size = 100
    from_item = 0

    while True:
        params = {
            'from': from_item,
            'size': size
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            if not data:
                break
            for item in data:
                address = item['address']
                balance = int(item['balance'])
                if address in holders:
                    holders[address] += balance
                else:
                    holders[address] = balance
            from_item += size
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return None

    return holders

def save_holders_to_csv(holders, filename):
    """
    Saves the list of holders to a CSV file.

    Args:
        holders (dict): The dictionary of holders with addresses and balances.
        filename (str): The name of the CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['address', 'balance'])
        for address, balance in holders.items():
            writer.writerow([address, balance])
    logging.info(f"Holders saved to {filename}")

if __name__ == "__main__":
    collection_id = 'CROMDAO-ad2e12'
    holders = get_holders(collection_id)
    if holders is not None:
        logging.info(f"Total holders retrieved: {len(holders)}")
        
        # Save holders to CSV file
        save_holders_to_csv(holders, 'holders.csv')
    else:
        logging.error("Failed to fetch the holders.")
