import requests
import time
import datetime
import telegram
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TOKEN)

def get_gold_price_usd():
    url = "https://api.metals.live/v1/spot/gold"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[0]["price"]
        return price
    except Exception as e:
        print("Errore ottenendo il prezzo dell’oro:", e)
        return None

def get_usd_to_eur_rate():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=EUR"
    try:
        response = requests.get(url)
        data = response.json()
        rate = data["rates"]["EUR"]
        return rate
    except Exception as e:
        print("Errore ottenendo il tasso di cambio:", e)
        return None

while True:
    gold_usd = get_gold_price_usd()
    rate = get_usd_to_eur_rate()

    if gold_usd and rate:
        gold_eur = gold_usd * rate
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        message = f"[{now}]
Prezzo oro:
- {gold_usd:.2f} USD/oz
- {gold_eur:.2f} EUR/oz"
        bot.send_message(chat_id=CHAT_ID, text=message)

    time.sleep(21600)  # ogni 6 ore
