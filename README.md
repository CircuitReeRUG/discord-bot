## Voltee
A discord bot which is made to keep track of events posted on the [Cover website](https://svcover.nl/) and announce them on discord.

## Usage
You need to have a discord bot token and `python >= 3.8`. You can get one by creating a new application on the [discord developer portal](https://discord.com/developers/applications) and adding a bot to it. You can then use the token to run the bot.
a
Clone the repo:
```bash
git clone https://github.com/CircuitReeRUG/voltee
```

Export the token as an environment variable:
```bash
export DISCORD_TOKEN="your_token_here"
```

Install the requirements:
```bash
cd voltee
pip install -r requirements.txt
```

Then you can run the bot by(assuming you are in the voltee directory):
```bash
cd src
python main.py
```

## Ideas
- [ ] Weather as channel name
- [ ] Channel with bus times
- [ ] Whatsapp integration(might be impossible)
