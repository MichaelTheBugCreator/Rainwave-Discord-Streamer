import asyncio
import logging
import os
import typing

from discord import FFmpegPCMAudio as ffmpeg
from discord.ext import commands

import settings
from StreamwaveStation import Streamwave

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
clients: typing.List[Streamwave] = [
        Streamwave(station) for station in settings.stations
    ]
try:
    for client in clients:
        loop.create_task(client.start(client.settings.discord_token))
    loop.run_forever()
except KeyboardInterrupt:
    for client in clients:
        try:
            loop.run_until_complete(client.logout())
        except:
            pass
finally:
    loop.close()
