# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

import Tkinter
import tkFont


_BaseString = ('This is a really boring basic string used for width '
               'calculations.')


class Widget(object):
    def __init__(self, widget, width):
        self._widget = widget
        if width is not None:
            font = tkFont.Font(font=widget.cget('font'))
            avg_char_width = font.measure(_BaseString) / len(_BaseString)
            self._widget.config(width=width / avg_char_width)

        self._widget.grid(column=0, sticky=Tkinter.W)


class Button(Widget):
    def __init__(self, master, text, button_handler, width=None):
        button = Tkinter.Button(master, text=text, command=button_handler)
        super(Button, self).__init__(button, width)
        self.set_text(text)

    def set_text(self, text):
        self._widget.config(text=text)


class Label(Widget):
    def __init__(self, master, text):
        label = Tkinter.Label(master, text=text)
        super(Label, self).__init__(label, None)
        self._widget.config(wraplength=350, justify=Tkinter.LEFT)

    def set_text(self, text):
        self._widget.config(text=text)


class Input(Widget):
    def __init__(self, master, text, input_handler, width):
        self._label = Label(master, text)
        self._content = Tkinter.StringVar()
        entry = Tkinter.Entry(master, textvariable=self._content)
        super(Input, self).__init__(entry, width)

        self._input_handler_fn = input_handler
        self._widget.bind('<Return>', self._input_handler)

    def _input_handler(self, _):
        if self._input_handler_fn is not None:
            self._input_handler_fn(self._content.get())

    def set_text(self, text):
        self._content.set(text)
