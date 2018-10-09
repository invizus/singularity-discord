# singularity-discord
Simple discord python bot

Implemented skills rpg-style mode:

Add your professions and level up, reach new levels and show off to everyone.

## Prerequisites:
python3

[discord.py](https://github.com/Rapptz/discord.py)

## config
in config.yml input your bot's token ID and your discord user ID to get some admin privileges

## How it works
* Stores data (prof title and experience) in JSON file.
* Calculates level out of accumulated experience using log(2) function.
* At the moment only one User ID is allowed to add new people into bot list using command `!initiate`
