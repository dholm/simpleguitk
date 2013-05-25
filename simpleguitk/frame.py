# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

import Tkinter
import sys
import tkFont

from .canvas import Canvas
from .control_objects import Button
from .control_objects import Input
from .control_objects import Label
from .input import InputAdapter
from .timers import destroy as destroy_timers


class Frame(object):
    def _create_root(self, title):
        root = Tkinter.Tk()
        root.wm_title(title)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        return root

    def _create_frame(self, width, height):
        frame = Tkinter.Frame(self._root, width=width, height=height)
        frame.grid()
        return frame

    def _create_canvas(self, width, height):
        frame = Tkinter.Frame(self._frame)
        frame.grid(column=1, rowspan=2)
        canvas = Canvas(frame, width, height)
        return (frame, canvas)

    def _create_control_frame(self, width):
        control_frame = Tkinter.Frame(self._frame, width=width)
        control_frame.grid(row=0, column=0)
        return control_frame

    def _create_status_frame(self):
        status_frame = Tkinter.Frame(self._frame)
        status_frame.grid(row=1, column=0)
        key_frame = Tkinter.LabelFrame(status_frame, text='Key:')
        key_frame.grid(row=0)
        mouse_frame = Tkinter.LabelFrame(status_frame, text='Mouse:')
        mouse_frame.grid(row=1)
        return (status_frame, key_frame, mouse_frame)

    def __init__(self, title, canvas_width, canvas_height, control_width):
        self._root = self._create_root(title)

        frame = self._create_frame(canvas_width, canvas_height)
        self._frame = frame

        (frame, canvas) = self._create_canvas(canvas_width, canvas_height)
        self._canvas_frame = frame
        self._canvas = canvas

        self._control_frame = self._create_control_frame(control_width)
        self._controls = []

        self._input = InputAdapter(self._root, self._canvas._get_widget())
        (stats, keys, mouse) = self._create_status_frame()
        self._stats_frame = stats
        self._key_frame = keys
        self._mouse_frame = mouse

    def _shutdown(self):
        destroy_timers()
        self._canvas.destroy()
        self._root.destroy()
        sys.exit(0)

    def start(self):
        try:
            self._root.mainloop()
        except KeyboardInterrupt:
            pass
        finally:
            self._shutdown()

    def set_draw_handler(self, draw_handler):
        self._canvas.set_draw_handler(draw_handler)

    def add_button(self, text, button_handler, width=None):
        button = Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)
        return button

    def add_label(self, text):
        label = Label(self._control_frame, text)
        self._controls.append(label)
        return label

    def add_input(self, text, input_handler, width):
        label = self.add_label(text)
        inp = Input(label, self._control_frame, input_handler, width)
        self._controls.append(inp)
        return inp

    def set_keydown_handler(self, key_handler):
        self._input.set_keydown_handler(key_handler)

    def set_keyup_handler(self, key_handler):
        self._input.set_keyup_handler(key_handler)

    def set_mouseclick_handler(self, mouse_handler):
        self._input.set_mouseclick_handler(mouse_handler)

    def set_mousedrag_handler(self, mouse_handler):
        self._input.set_mousedrag_handler(mouse_handler)

    def set_canvas_background(self, color):
        self._canvas.set_background(color)

    def get_canvas_textwidth(self, text, size, face='serif'):
        return tkFont.Font(size=size, family=face).measure(text)


def create_frame(title, canvas_width, canvas_height, control_width=200):
    return Frame(title, canvas_width, canvas_height, control_width)
