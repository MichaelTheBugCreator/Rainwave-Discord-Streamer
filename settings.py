#this is an example station settings file
#For each bot you want to start up, make a new StationSettings object
#in the array here, with the bot token, station ID, and station .ogg file
import logging
from typing import List
from settings_class import StationSettings

discord_log_level = logging.INFO
streamwave_log_level = logging.DEBUG

stations: List[StationSettings] = [
        StationSettings(
            discord_token="discord bot string token here",
            audio_source="http://relay.rainwave.cc/all.ogg",
            audio_channel="discord audio channel ID here",
            sid=5, #sid can be found at http://rainwave.cc/api4/
        ),
]
