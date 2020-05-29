from __future__ import absolute_import, unicode_literals

from pytify.dbus.metadata import Metadata
from pytify.dbus.interface import Interface


class Linux:
    def __init__(self):
        self.interface = Interface.factory('org.mpris.MediaPlayer2.Player')

        self.metadata = Metadata()

    def next(self):
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()

    def get_current_playing(self):
        return self.metadata.get_current_playing()
