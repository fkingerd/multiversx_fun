import json
import requests


baseUrl = 'https://gateway.elrond.com/address'


erd_addresses = {'YOUR_NAME':'YOUR_ERD'}


def get_balance(erd_address):
    get_bal = requests.get(f'{baseUrl}/{erd_address}/balance')
    json_transformation = json.loads(get_bal.text)
    raw_balance = json_transformation['data']['balance']
    power_of_ten = len(raw_balance)
    balance = "your eGOLD balance is: {:.4f}".format(int(raw_balance)/10**(power_of_ten + (18 - power_of_ten)))

    return balance


def get_esdt():
    with open('your_esdts.txt', 'w+') as file:
        for name, erd in erd_addresses.items():
            how_many_nfts = 0
            file.write(f'{name} {get_balance(erd)}\n')
            file.write(f'{name} these are your ESDTs:\n')
            get_esdts = requests.get(f'{baseUrl}/{erd}/esdt')
            json_transformation = get_esdts.json()
            for key, value in json_transformation['data']['esdts'].items():
                file.write(f'\t{key}\n')
                how_many_nfts += 1
                for key1, value1 in json_transformation['data']['esdts'][key].items():
                    if key1 == 'royalties':
                        value1 = "{:.0f}".format(int(value1) / 100) + '%'
                    if key1 == 'name' \
                    or key1 == 'balance' \
                    or key1 == 'creator' \
                    or key1 == 'royalties' \
                    or key1 == 'tokenIdentifier':
                        file.write(f'\t\t{key1}' +
                                   ' ' * (15 - len(key1)) +
                                   f'\t{value1}\n')
                file.write('\n')
            file.write(f'Total ESDTs are: {how_many_nfts}\n')


get_esdt()
