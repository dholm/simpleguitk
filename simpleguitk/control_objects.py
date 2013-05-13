import Tkinter


class Button(object):
    def __init__(self, master, text, button_handler, width=None):
        self._button = Tkinter.Button(master, text=text,
                                      command=button_handler)
        self._button.grid(column=0)
