# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

import io
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


class Sound(object):
    def __init__(self, url, channel):
        import pygame
        self._channel = pygame.mixer.Channel(channel)
        soundfile = urlopen(url).read()
        self._sound = pygame.mixer.Sound(io.BytesIO(soundfile))
        self._paused = False

    def play(self):
        if self._paused:
            self._paused = False
            self._channel.unpause()
        else:
            self._channel.play(self._sound)

    def pause(self):
        self._channel.pause()
        self._paused = True

    def rewind(self):
        self._channel.stop()

    def set_volume(self, volume):
        self._channel.set_volume(volume)

MAX_CHANNELS = 32
_initialized = False
_next_channel = 0


def sound_init():
    global _initialized
    import pygame
    pygame.mixer.init()
    pygame.mixer.set_num_channels(MAX_CHANNELS)
    _initialized = True


def load_sound(URL):
    global _next_channel
    if not _initialized:
        sound_init()

    _next_channel += 1
    return Sound(URL, _next_channel - 1)
