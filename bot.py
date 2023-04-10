import discord
import os
from discord import app_commands
from typing import Optional

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.default()
bot = MyClient(intents=intents)

if os.path.exists("token.txt"):
    token = open("token.txt", "r").readline()
else:
    token = os.environ['DISCORD_BOT_TOKEN']

def get_file_names(directory_path):
    files = os.listdir(directory_path)
    file_names = []
    for file in files:
        file_path = os.path.join(directory_path, file)
        if not os.path.isdir(file_path):
            file_name, file_extension = os.path.splitext(file)
            file_names.append(file_name)

    return file_names

def list_to_string(list_: list):
    sorted_list = sorted(list_)
    return '\n'.join(str(item) for item in sorted_list)

@bot.event
async def on_ready():
    invite_link = f'https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=bot%20applications.commands'
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f'Invite me using this link: {invite_link}')
    await bot.change_presence(activity=discord.Game(name="with soundboard"))

@bot.event
async def on_guild_join(guild):
    print(f"Joined {guild.name}")

@bot.tree.command()
async def list(interaction: discord.Interaction):
    """
    List all available sound files
    """
    file_names = get_file_names("./sounds/")
    if file_names is None:
        await interaction.response.send_message(f'{interaction.user.mention} No sound files found..')
        return
    list_ = list_to_string(file_names)
    await interaction.response.send_message(f'```{list_}```')

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    """
    I will mention you <3
    """
    print(f'{interaction.user.mention} used ping')
    await interaction.response.send_message(f'Hi {interaction.user.mention}')

@bot.tree.command()
async def input(interaction: discord.Interaction, arg: str):
    """
    I will repeat after you
    """
    print(f"{interaction.user} used input")
    await interaction.response.send_message(f"You typed: {arg}")

@bot.tree.command()
async def join(interaction: discord.Interaction):
    """
    Summon me to your voice channel
    """
    voice_channel = interaction.user.voice.channel

    if voice_channel is None:
        await interaction.response.send_message(f"{interaction.user.mention} You are not in a voice channel. Hop in one first!")
        return

    await interaction.response.send_message('Joined voice channel')
    await voice_channel.connect()

@bot.tree.command()
async def leave(interaction: discord.Interaction):
    """
    I will stop and leave the voice channel
    """
    voice_client = interaction.guild.voice_client

    if voice_client is None:
        await interaction.response.send_message(f"{interaction.user.mention} I am not in a voice channel right now..")
        return

    await interaction.response.send_message('Left voice channel')
    await voice_client.disconnect()

@bot.tree.command()
async def play(interaction: discord.Interaction, *, query: str, volume: Optional[int] = 25):
    """
    I will play a sound
    """
    voice_channel = interaction.user.voice.channel
    if voice_channel is None:
        await interaction.response.send_message(f"{interaction.user.mention} You are not in a voice channel. Hop in one first!")
        return

    if interaction.guild.voice_client is None:
        await voice_channel.connect()

    await interaction.response.send_message(f'Playing {query}')
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f'./sounds/{query}.mp3'))
    source.volume = volume / 100
    interaction.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

bot.run(token)
