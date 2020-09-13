from __future__ import absolute_import, unicode_literals

from pytify.dbus.metadata import Metadata
from pytify.dbus.interface import Interface

import logging

logger = logging.getLogger(__name__)


class CustomMetadata(Metadata):
    def get_current_playing(self):
        playing = {}

        for key, value in self.get_metadata().items():
            if key == 'xesam:album':
                playing['album'] = value

            elif key == 'xesam:title':
                playing['title'] = value

            elif key == 'xesam:artist':
                playing['artist'] = value[0]

        return f"{playing['title']} - {playing['artist']}"


class Linux:
    def __init__(self):
        self.interface = Interface.factory('org.mpris.MediaPlayer2.Player')

        self.metadata = CustomMetadata()

    def next(self):
        print("next song")
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()

    def get_current_playing(self):
        return self.metadata.get_current_playing()
