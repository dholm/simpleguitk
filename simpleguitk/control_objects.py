import Tkinter


class Button(object):
    def __init__(self, master, text, button_handler, width=None):
        self._button = Tkinter.Button(master, text=text, width=width,
                                      command=button_handler)
        self._button.grid(column=0)

    def set_text(self, text):
        self._button.config(text=text)


class Label(object):
    def __init__(self, master, text):
        self._label = Tkinter.Label(master, text=text)
        self._label.grid(column=0)

    def set_text(self, text):
        self._label.config(text=text)


class Input(object):
    def __init__(self, label, master, input_handler, width):
        self._label = label
        self._content = Tkinter.StringVar()
        self._entry = Tkinter.Entry(master, width=width,
                                    textvariable=self._content)
        self._entry.bind('<Return>', input_handler)
        self._entry.grid(column=0)

    def set_text(self, text):
        self._content.set(text)
