import discord
import os
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == '?regras':
          await message.channel.send(f'{message.author.name} as regras são essas:{os.linesep} 1-Nunca xingue um membro do gp {os.linesep} 2-Você tem o direito de defesa antes de ser banido')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTIxMzY1MjMwMjY2NjQwMzg1MA.GsTH7V.hlKwDTNsyhAmOfqLXfhZa8zpI0xpCiLSjCRIPs')