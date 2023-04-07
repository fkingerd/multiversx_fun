import tweepy
import config
import requests
import os


os.chdir('to/where/the/script/lies')

authenticate = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET_KEY)
authenticate.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticate, wait_on_rate_limit=True)
# get_all_coins = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=false')


def get_previous_values(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            previous_values = [tuple(map(float, line.strip().split(','))) for line in file.readlines()]
    else:
        previous_values = None

    return previous_values

def save_current_values(file_name, current_values):
    with open(file_name, 'w') as file:
        for value in current_values:
            file.write(f'{value[0]},{value[1]}\n')

def get_coin_values():
    coins = ['elrond-erd-2', 'cardano']
    values = []

    for coin in coins:
        r = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd%2Ceur&include_last_updated_at=%20')
        format_json = r.json()

        coin_usd_value = round(format_json[coin]['usd'], 2)
        coin_eur_value = round(format_json[coin]['eur'], 2)
        values.append((coin_usd_value, coin_eur_value))

    return values

def format_twitter_post(coin_values, previous_values):
    coin_names = ['eGLD', 'ADA']
    coin_emojis = ['⚡️', '❈']
    lines = ["💹 Crypto Market Update 🚀"]
    
    for i, (usd, eur) in enumerate(coin_values):
        if previous_values is not None:
            if usd > previous_values[i][0]:
                trend_usd = "📈"
            elif usd < previous_values[i][0]:
                trend_usd = "📉"
            else:
               trend_usd = "📊"
            
            if eur > previous_values[i][1]:
                trend_eur = "📈"
            elif eur < previous_values[i][1]:
                trend_eur = "📉"  
            else:
                trend_eur = "📊" 
        else:
            trend_usd, trend_eur = "🔹", "🔹"

        lines.append(f"\n{coin_emojis[i]} ${coin_names[i]} 💎")
        lines.append(f"  {trend_usd} {usd} $USD 💵")
        lines.append(f"  {trend_eur} {eur} $EUR 💶\n")

    lines.append("👀 Updates every 6 hours! 👀\n#LfkinGo #MVX #Cardano")
    return "\n".join(lines)

previous_values_file = 'previous_values.txt'
previous_values = get_previous_values(previous_values_file)

coin_values = get_coin_values()

save_current_values(previous_values_file, coin_values)
twitter_post = format_twitter_post(coin_values, previous_values)

# print(twitter_post)

api.update_status(twitter_post)
