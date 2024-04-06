import requests
import csv
from time import sleep

# Function to check and write non-SC addresses to a CSV file
def process_addresses_and_write_to_csv(coin_symbol):
    from_value = 0
    total_processed = 0

    with open('filtered_addresses_and_balances.csv', 'w', newline='') as csvfile:
        fieldnames = ['Address'] # , 'Balance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        while True:
            url = f"https://api.elrond.com/tokens/{coin_symbol}/accounts?from={from_value}&size=999"
            try:
                response = requests.get(url)
                response.raise_for_status()
                sleep(1)
            except Exception as e:
                print(f"Error fetching data: {e}")
                break
            
            data = response.json()
            if not data:
                print("No more data to process.")
                break
            
            for item in data:
                address = item.get("address")
                # balance = item.get("balance")
                
                # Check if the address is a non-SC address
                account_url = f"https://api.elrond.com/accounts/{address}"
                try:
                    account_response = requests.get(account_url)
                    account_response.raise_for_status()
                    account_data = account_response.json()
                    sleep(1)
                except Exception as e:
                    print(f"Error fetching account data: {e}")
                    continue
                
                if "ownerAddress" not in account_data and "assets" not in account_data and "code" not in account_data:
                    writer.writerow({'Address': address}) # , 'Balance': balance})
                    total_processed += 1
                
                print(f"In progress total non-SC processed: {total_processed}\n")
            
            print(f"Processed {len(data)} addresses, Total non-SC processed: {total_processed}")
            from_value += 999
            # Adding a short delay can help avoid hitting rate limits
            sleep(60)

# Execute the function with the desired coin symbol
process_addresses_and_write_to_csv("HIT-3f109b")
