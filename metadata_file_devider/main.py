# libraries to use
import json
from pathlib import Path


def create_metadata_files(big_meadata_filename: str): # the file should be like so 'metadata.json'
    # getting your path to where the script is
    main_dir_path = str(Path.cwd())

    #opening the file to read
    with open(big_meadata_filename, 'r') as input_file:
        
        # loading the content of the file
        data_to_parse = json.load(input_file)

        # iterating through the content
        for item in range(0, len(data_to_parse)):
            # the content of interest
            paste = data_to_parse[item]

            # if you want the resulting files to be like 0001.json, 0002.json ....5000.json 
            # if the collection has more than 9999 then you need to edit with 5 for the zfill function
            # filename = f"{str(paste['edition']).zfill(4)}.json"

            # if you want the resulting files to be like 1.json, 2.json ....5000.json 
            filename = f"{str(paste['edition'])}.json"

            # the dir where to export the resulting files
            metadata_dir = main_dir_path + '/metadata_files' + f'/{filename}'

            # creating the resulting file
            with open(metadata_dir, "w") as file:
                json.dump(paste, file)

# calling the function to create the files
create_metadata_files('metadata.json')