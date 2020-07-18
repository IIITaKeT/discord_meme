import discord
import asyncio
import requests

DISCORD_BOT_TOKEN = 'NTk4MjM4OTA0NTc0ODA0Mjk0.XSTvcw.9IGU3GCSq3cd-dEJWeH9f1-sTpE'

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!btcprice'):
        print('[command]: btcprice ')
        btc_price_usd, btc_price_rub = get_btc_price()
        await client.send_message(message.channel, 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub))

def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice

client.run(DISCORD_BOT_TOKEN)