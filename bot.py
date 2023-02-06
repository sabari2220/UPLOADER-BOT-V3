
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from plugins.config import Config

from pyrogram import Client as Ntbot
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Ntbot = Ntbot(
        "Uploader Bot",
        bot_token="5753542938:AAFQ_23zAEwxGTPRAEMCItqm1Vz6BjEfjXU",
        api_id="29161994",
        api_hash="6de0c3c108577f72d5a50097108e9486",
        plugins=plugins)
    Ntbot.run()
