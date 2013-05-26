# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

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
        self._input_handler_fn = input_handler
        self._entry.bind('<Return>', self._input_handler)
        self._entry.grid(column=0)

    def _input_handler(self, _):
        if self._input_handler_fn is not None:
            self._input_handler_fn(self._content.get())

    def set_text(self, text):
        self._content.set(text)
