import requests
from collections import Counter


def get_twitter_handle(url):
    if url:
        twitter_url_parts = url.split("/")
        if len(twitter_url_parts) > 0:
            return "@" + twitter_url_parts[-1]
    return ""


erd_wallet = 'erd1qqqqqqqqqqqqqpgq569sz97ue8znu8vv728ygm3dnrd59qe827rstm3ylp'
base_api_url = f'https://api.multiversx.com/accounts/{erd_wallet}'

tokens = requests.get(f'{base_api_url}/tokens')
tokens_unparsed = tokens.json()

nfts = requests.get(f'{base_api_url}/nfts')
nfts_unparsed = nfts.json()

social_handles = {}

for nft in nfts_unparsed:
    ticker = nft.get("ticker", "").split("-")[0]
    social_data = nft.get("assets", {}).get("social")
    twitter_handle = get_twitter_handle(social_data.get("twitter")) if social_data else None
    if ticker:
        if twitter_handle:
            social_handles[ticker] = twitter_handle
        else:
            social_handles[ticker] = ""


ticker_counts = Counter(
    j.get("ticker").split("-")[0] if j.get("ticker") else j.get("name", "")
    for j in nfts_unparsed
)

with open('output.txt', 'w') as f:
    f.write('\tTokens held!\n')

    for token in tokens_unparsed:
        decimals = 10 ** token['decimals']
        raw_balance = int(token['balance'])
        balance = f'{raw_balance / decimals:,.2f}'
        f.write(f"{token['name']}: {balance}\n")

    f.write('\n\tNFTs held!\n')

    for ticker, count in ticker_counts.items():
        social_handle = social_handles.get(ticker)
        if social_handle:
            f.write(f"{social_handle}: {count}\n")
        else:
            f.write(f"{ticker}: {count}\n")
