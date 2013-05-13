import Tkinter

from .canvas import Canvas
from .control_objects import Button


class Frame(object):
    def __init__(self, title, canvas_width, canvas_height, control_width):
        self._root = Tkinter.Tk()
        self._root.wm_title(title)
        self._root.protocol('WM_DELETE_WINDOW', self._shutdown)

        self._frame = Tkinter.Frame(self._root)
        self._frame.grid()
        self._frame.rowconfigure('all', minsize=canvas_height, pad=3)
        self._frame.columnconfigure('all', pad=3, minsize=control_width)
        self._frame.columnconfigure('all', pad=3, minsize=canvas_width)

        self._canvas_frame = Tkinter.Frame(self._frame)
        self._canvas_frame.grid(column=1, rowspan=2)
        self._canvas = Canvas(self._canvas_frame, canvas_width, canvas_height)

        self._control_frame = Tkinter.Frame(self._frame)
        self._control_frame.grid(row=0, column=0)
        self._controls = []

        self._status_frame = Tkinter.Frame(self._frame)
        self._status_frame.grid(row=1, column=0)
        self._key_frame = Tkinter.LabelFrame(self._status_frame, text='Key:')
        self._key_frame.grid(row=0)
        self._mouse_frame = Tkinter.LabelFrame(self._status_frame,
                                               text='Mouse:')
        self._mouse_frame.grid(row=1)

    def _shutdown(self):
        self._canvas._shutdown()
        self._root.destroy()

    def start(self):
        self._root.mainloop()

    def set_draw_handler(self, draw_handler):
        self._canvas.set_draw_handler(draw_handler)

    def add_button(self, text, button_handler, width=None):
        button = Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)


def create_frame(title, canvas_width, canvas_height, control_width=200):
    return Frame(title, canvas_width, canvas_height, control_width)
