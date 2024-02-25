import requests
import discord
from datetime import date
import threading



# Configura tu API key de Google News
API_KEY = ""

# Configura tu token de acceso de Discord
DISCORD_TOKEN = ""

# Canal de Discord donde se enviarán las notificaciones
CHANNEL_ID = "int"

SERVER_ID = "int"

fecha_actual = date.today()


q = "checo perez"
TodayDate = ""#fecha_actual.strftime("%Y-%m-%d")
sort = "publishedAt"
lang = "es"
size = "5"

def get_news():
  """Obtiene las últimas noticias sobre Fórmula 1."""
  url = "https://newsapi.org/v2/everything?q={}&from={}&sortBy={}&language={}&apiKey={}&pagesize={}".format(q, TodayDate, sort, lang, API_KEY, size)
  response = requests.get(url)
  data = response.json()
  return data["articles"]

# Define the intents you need
intents = discord.Intents().default()
# Create the client with the intents argument

def send_notification(news):
  """Envía una notificación a Discord."""
  client = discord.Client(intents=intents)

  #print(client)

  @client.event
  async def on_ready():
    '''
    guild = client.get_guild(SERVER_ID)  # Reemplaza GUILD_ID con el ID del servidor
    channels = await guild.fetch_channels()
    print(channels)
    for channel in channels:
        print(channel.name)
    '''
    
    channel = client.get_channel(CHANNEL_ID)
    #print(channel)
    if channel:
        # Send the message only if the channel exists

        for article in news:
            embed = discord.Embed(title=article["title"], description=article["description"], url=article["url"])
            await channel.send(embed=embed)
        await client.close()
    else:
        # Handle the case where the channel is not found
        print("Channel not found!")
    

  client.run(DISCORD_TOKEN)
  #client.close()

if __name__ == "__main__":
  news = get_news()
  send_notification(news)
