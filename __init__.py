from plugins.plugin import SarlaccPlugin
from configparser import ConfigParser
import os
import requests

class Plugin(SarlaccPlugin):
    def run(self):
        self.logger.info("Loading malshare plugin")

        # Read config
        self.config = ConfigParser()
        self.config.readfp(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "malshare.cfg")))
        self.config.read(["smtpd.cfg",])


    async def new_attachment(self, _id, sha256, content, filename, tags):
        self.logger.info("Uploading new sample to malshare. SHA256: %s", sha256)

        requests.post(url="https://malshare.com/api.php?api_key={}&action=upload".format(self.config["malshare"]["key"]),
                files={filename: content})

