# Discord Soundboard Bot

This is a Python Discord bot that plays sound files in voice channels.

## Installation

1. Install Python 3.8 or later
2. Install the discord.py library with `python3 -m pip install -U discord.py[voice]`
3. Clone the repository or download the source code
4. Create a file called `token.txt` in the root directory and paste your bot token inside it
5. Create a directory called `sounds` in the root directory and add your sound files in `.mp3` format

## Usage

1. Start the bot by running the `bot.py` file using `python bot.py`
2. Invite the bot to your server using the invite link provided in the console
3. In any text channel, use one of the available commands to play a sound in your voice channel

### Available Commands

- `/list`: Lists all available sound files
- `/ping`: Mentions the user who called the command
- `/input [arg]`: Repeats the argument passed by the user
- `/join`: Joins the user's current voice channel
- `/leave`: Leaves the current voice channel
- `/play [query] [volume]`: Plays the sound file with the given name in the current voice channel. The optional `volume` parameter is a number between 0 and 100.

## Contributing

If you find any bugs or issues with the bot, feel free to open an issue or submit a pull request.
