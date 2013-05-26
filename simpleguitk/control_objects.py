# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

import Tkinter
import tkFont


class Widget(object):
    def _config_width(self, text):
        if self._width is not None and len(text):
            font = tkFont.Font(font=self._widget.cget('font'))
            avg_char_width = font.measure(text) / len(text)
            width = self._width / avg_char_width
            self._widget.config(width=width)

    def __init__(self, widget, width):
        self._widget = widget
        self._width = width
        self._widget.grid(column=0)


class Button(Widget):
    def __init__(self, master, text, button_handler, width=None):
        button = Tkinter.Button(master, text=text, command=button_handler)
        super(Button, self).__init__(button, width)
        self._config_width(text)

    def set_text(self, text):
        self._widget.config(text=text)
        self._config_width(text)


class Label(Widget):
    def __init__(self, master, text):
        label = Tkinter.Label(master, text=text)
        super(Label, self).__init__(label, None)
        text_width = max(len(text), 15)
        self._widget.config(width=text_width)

    def set_text(self, text):
        self._widget.config(text=text)


class Input(Widget):
    def __init__(self, master, text, input_handler, width):
        self._label = Label(master, text)
        self._content = Tkinter.StringVar()
        entry = Tkinter.Entry(master, textvariable=self._content)
        super(Input, self).__init__(entry, width)
        self._config_width(text)

        self._input_handler_fn = input_handler
        self._widget.bind('<Return>', self._input_handler)

    def _input_handler(self, _):
        if self._input_handler_fn is not None:
            self._input_handler_fn(self._content.get())

    def set_text(self, text):
        self._content.set(text)
