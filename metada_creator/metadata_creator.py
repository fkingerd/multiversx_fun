import json
import os


trait_qty = int(input('How many traits do you want?\nInput a number: '))


trait_names = []
for i in range(trait_qty):
    trait_name = input(f"Enter a name for trait #{i+1}: ")
    trait_names.append(trait_name)


nft_qty = int(input('How many NFTs does your collection hold?\nInput a number: '))


def json_creator():
    dir_name = input("Enter a name for the directory to store the JSON files: ")
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    else:
        i = 1
        while os.path.exists(f"{dir_name}_{i}"):
            i += 1
        dir_name = f"{dir_name}_{i}"
        os.makedirs(dir_name)

    for nft in range(nft_qty):
        name = f"XXXXXXXXX #{nft + 1}"
        description = "XXXXXXXXX_Description"
        edition = nft + 1
        attributes = []
        for j in range(trait_qty):
            # value = input(f"Enter a value for trait '{trait_names[j]}' in NFT #{i+1}: ") # This can be used to add directly the value from cli eficient only for small number of nft_qty
            value = ''
            attributes.append({"trait_type": trait_names[j], "value": value})
        nft_traits_json = {"name": name, "description": description, "edition": edition, "attributes": attributes}
        with open(os.path.join(dir_name, f"{nft + 1}.json"), "w") as f:
            json.dump(nft_traits_json, f, indent=4)

json_creator()
