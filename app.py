# Basic flask imports
from flask import Flask, request, json
from dotenv import load_dotenv
import discord
import os

load_dotenv()

app = Flask(__name__)
client = discord.Client()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DEBUG=True


@app.route('/')
def index():
    result = {'hello': 'hello'}
    return json.jsonify()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#     bot_id = client.user.id

# @client.event
# async def on_ready(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run(BOT_TOKEN)
    app.run(debug=DEBUG)