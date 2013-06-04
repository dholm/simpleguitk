# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

import io
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


class Sound(object):
    def __init__(self, url):
        import pygame
        self._channel = None
        if url.startswith('http'):
            soundfile = urlopen(url).read()
        else:
            soundfile = open(url).read()
        self._sound = pygame.mixer.Sound(io.BytesIO(soundfile))
        self._paused = False

    def play(self):
        self._paused = False
        if self._channel is not None:
            if not self._channel.get_busy():
                self._channel.play(self._sound)
            elif self._paused:
                self._channel.unpause()
        else:
            self._channel = self._sound.play()

    def pause(self):
        if self._channel is not None:
            self._paused = True
            self._channel.pause()

    def rewind(self):
        if self._channel is not None:
            self._channel.stop()

    def set_volume(self, volume):
        self._sound.set_volume(volume)

_initialized = False


def sound_init():
    global _initialized
    import pygame
    pygame.mixer.init()
    _initialized = True


def load_sound(URL):
    global _next_channel
    if not _initialized:
        sound_init()

    return Sound(URL)
