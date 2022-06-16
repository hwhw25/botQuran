import discord
import os
import requests
import random

client = discord.Client()
embed = discord.Embed()
def get_ayat(ayat):
  url = 'http://api.alquran.cloud/ayah/'+str(ayat)+'/editions/quran-uthmani,en.pickthall'
  json_data = requests.get(url).json()
  ayatArab = json_data['data'][0]['text']
  ayatEng = json_data['data'][1]['text']
  surat = json_data['data'][0]['surah']['englishName']+\
           '('+str(json_data['data'][0]['surah']['number'])+'):'+\
           str(json_data['data'][0]['numberInSurah'])
  return[ayatArab,ayatEng,surat]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$tes'):
    ayat = random.randint(1,6237)
    isi = get_ayat(ayat)
    embed.title
    embedVar = discord.Embed(title="بسم الله الرحمن الرحيم", description=isi[0], color=0x00ff00)
    embedVar.add_field(name=isi[2], value=isi[1], inline=False)
    await message.channel.send(embed=embedVar)

client.run(os.getenv('TOKEN'))
