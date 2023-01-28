import requests # don't forget to install this lib, from terminal: pip install requests
from PIL import Image # don't forget to install this lib, from terminal: pip install pillow


def get_png_from_nft(erd: str, collection: str):
    mx_api_url = requests.get(f'https://api.multiversx.com/accounts/{erd}/nfts?size=123&collections={collection}')
    
    # geting the result in json format
    to_parse = mx_api_url.json()
    for item in range(0, len(to_parse)):    # parsing through the json format and looking for the particular key that holds the url
        img_url = to_parse[item]['media'][0]['url']    # get the url
        img = Image.open(requests.get(img_url, stream = True).raw)    # get the image behind the url
        
        # checking if the name of the .png file is made of 1, 2, 3 or 4 digit number
        if len(img_url) == 88:
            img.save(f'{img_url[-5:]}')    # 1 digit: 5.png
        elif len(img_url) == 89:
            img.save(f'{img_url[-6:]}')    # 2 digit: 55.png
        elif len(img_url) == 90:
            img.save(f'{img_url[-7:]}')    # 3 digit: 5555.png
        elif len(img_url) == 91:
            img.save(f'{img_url[-8:]}')    # 4 digit: 55555.png
        else:
            return f'There are 0 {collection} NFTs held in wallet: {erd}.'    # the erd has no nfts of the specified collection

'''
Example of how to call the function:

get_png_from_nft('erd1xuf43l9v4d3lxhfg9ehzh244592gf2an7hmuw9h84gma7j8fdsws60rrqn', 'MRG-1c3ba4')

replace the placeholders from below as shown above
'''
get_png_from_nft(enter_erd_here, enter_nft_collection_here)    # the actual call of the function above
