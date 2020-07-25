# singularity-discord
Simple discord python bot.

RPG-style leveling up your skills.

Define profession, add experience and achieve new levels.

## Prerequisites:
python3

PyYAML

[discord.py](https://github.com/Rapptz/discord.py)

## singularity-data files
Rename database.json.example to database.json

Rename config.yml.example to config.yml

### config.yml
in config.yml set:
- bot token ID
- discord user ID who will have admin privileges
- path to database.json can stay same

## Build & run
```
git clone https://github.com/invizus/singularity-discord
cd singularity-discord
docker build . -t singularity:v402
docker-compose up -d
```

## How it works
* Stores data (prof title and experience) in JSON file.
* Calculates level out of accumulated experience using log(2) function.
* At the moment only one User ID is allowed to add new people into bot list using command `!initiate`
