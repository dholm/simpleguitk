class KeyMap(object):
    def __getitem__(self, name):
        return name.lower()


KEY_MAP = KeyMap()


class Input(object):
    def __init__(self, master):
        self._keydown_handler = None
        self._keyup_handler = None
        master.bind('<KeyPress>', self._keydown)
        master.bind('<KeyRelease>', self._keyup)

    def _keydown(self, key):
        if self._keydown_handler is not None:
            self._keydown_handler(key.keysym.lower())

    def _keyup(self, key):
        if self._keyup_handler is not None:
            self._keyup_handler(key.keysym.lower())

    def set_keydown_handler(self, key_handler):
        self._keydown_handler = key_handler

    def set_keyup_handler(self, key_handler):
        self._keyup_handler = key_handler
