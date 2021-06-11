import requests
from dotenv import load_dotenv
import os
load_dotenv()


APP_ID = os.getenv('APP_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')

print(BOT_TOKEN)
url = "https://discord.com/api/v8/applications/{APP_ID}/commands".format(APP_ID=APP_ID)
headers = {"Authorization": "Bot {BOT_TOKEN}".format(BOT_TOKEN=BOT_TOKEN)}
print(headers)


json = {
    "name": "blep",
    "description": "Send a random adorable animal photo",
    "options": []
}


# json = {
#     "name": "tickers",
#     "description": "Get information on tickers based on screener",
#     "options": [
#         {
#             "name": "squeezed",
#             "description": "Get tickers that are being squeezed",
#             "type": 1
#         },
#         {
#             "name": "unusual volume",
#             "description": "Get tickers that have unusual volume",
#             "type": 2
#         },
#         {
#             "name": "top gainers",
#             "description": "Get top gainer tickers",
#             "type": 3
#         },
#         {
#             "name": "insider buy",
#             "description": "Get tickers that have a lot of insiders buying",
#             "type": 4
#         },
#         {
#             "name": "sleeping monster",
#             "description": "Get tickers that fit under 'sleeping monster'",
#             "type": 5
#         },
#         {
#             "name": "crossing ma50",
#             "description": "Get tickers that are crossing MA 50 uptrend",
#             "type": 6
#         },
#         {
#             "name": "best",
#             "description": "Get tickers that fit in TWO or more of the screeners",
#             "type": 7
#         }

#     ]
# }

r = requests.put(url, headers=headers, json=json)
print(r)
