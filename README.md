# Rainwave-Discord-Streamer
A simple bot that streams music from Rainwave to Discord

Streamwave.py is an all-around bot designed to connect to any Rainwave channel a user wishes and start playing music. The bot will automatically connect to the voice channel the user is in. Possible commands are !play, !stop, and !h, for starting, stopping, and displaying the help text appropriately. Arguments to the !play command may be given to specify which Rainwave channel to connect to. Possible arguments are "covers", "ocr", "game", and "chiptune". The arguments do not have fuzzy matching, and if there is an incorrect argument given, the bot will default to the All channel.

StreamwaveGame.py is a more narrowly-designed bot to connect to hard-coded channel IDs when user(s) are in the channel(s). In addition, the bot is designed to only play one Rainwave channel, and will not take any arguments. Other Streamwave(Channel).py files exist to run bots for the other Rainwave channels, but they are pretty much just copy-and-paste versions of StreamwaveGame, with channel ID, bot token, and music source all having different values.
