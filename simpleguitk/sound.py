import urllib


class Sound(object):
    def __init__(self, url):
        import pygame
        soundfile = urllib.urlretrieve(url)[0]
        self._sound = pygame.mixer.Sound(soundfile)

    def play(self):
        self._sound.play()

    def pause(self):
        self._sound.pause()

    def rewind(self):
        self._sound.rewind()

    def set_volume(self, volume):
        self._sound.set_volume(volume)

_initialized = False


def sound_init():
    global _initialized
    import pygame
    pygame.mixer.init()
    _initialized = True


def load_sound(URL):
    if not _initialized:
        sound_init()

    return Sound(URL)
