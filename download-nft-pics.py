import requests # don't forget to install this lib, from terminal: pip install requests
from PIL import Image # don't forget to install this lib, from terminal: pip install pillow


def get_png_from_nft(erd: str, collection: str):
    x = requests.get(f'https://api.multiversx.com/accounts/{erd}/nfts?size=123&collections={collection}')

    to_parse = x.json()
    for x in range(0, len(to_parse)):
        img_url = to_parse[x]['media'][0]['url']
        img = Image.open(requests.get(img_url, stream = True).raw)
        
        if len(img_url) == 88:
            img.save(f'{img_url[-5:]}')
        elif len(img_url) == 89:
            img.save(f'{img_url[-6:]}')
        elif len(img_url) == 90:
            img.save(f'{img_url[-7:]}')
        elif len(img_url) == 91:
            img.save(f'{img_url[-8:]}')
        else:
            return f'There are 0 {collection} NFTs held in wallet: {erd}.'

# Example of how to call the function:
# get_png_from_nft('erd1xuf43l9v4d3lxhfg9ehzh244592gf2an7hmuw9h84gma7j8fdsws60rrqn', 'MRG-1c3ba4')
# replace the placeholders from below as shown above
get_png_from_nft(enter_erd_here, enter_nft_collection_here)
