class KeyMap(object):
    def __getitem__(self, name):
        return name.lower()


KEY_MAP = KeyMap()


class Input(object):
    def __init__(self, keyboard_master, mouse_master):
        self._keydown_handler = None
        self._keyup_handler = None
        keyboard_master.bind('<KeyPress>', self._keydown)
        keyboard_master.bind('<KeyRelease>', self._keyup)

        self._mouse_click_handler = None
        mouse_master.bind('<Button-1>', self._mouse_click)

    def _keydown(self, key):
        if self._keydown_handler is not None:
            self._keydown_handler(key.keysym.lower())

    def _keyup(self, key):
        if self._keyup_handler is not None:
            self._keyup_handler(key.keysym.lower())

    def _mouse_click(self, event):
        if self._mouse_click_handler is not None:
            self._mouse_click_handler((event.x, event.y))

    def set_keydown_handler(self, key_handler):
        self._keydown_handler = key_handler

    def set_keyup_handler(self, key_handler):
        self._keyup_handler = key_handler

    def set_mouseclick_handler(self, mouse_handler):
        self._mouse_click_handler = mouse_handler
