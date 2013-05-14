import Tkinter

from .canvas import Canvas
from .control_objects import Button


class Frame(object):
    def _create_root(self, title):
        root = Tkinter.Tk()
        root.wm_title(title)
        root.protocol('WM_DELETE_WINDOW', self._shutdown)
        return root

    def _create_frame(self, canvas_width, canvas_height, control_width):
        frame = Tkinter.Frame(self._root)
        frame.grid()
        frame.rowconfigure('all', minsize=canvas_height, pad=3)
        frame.columnconfigure('all', pad=3, minsize=control_width)
        frame.columnconfigure('all', pad=3, minsize=canvas_width)
        return frame

    def _create_canvas(self, width, height):
        frame = Tkinter.Frame(self._frame)
        frame.grid(column=1, rowspan=2)
        canvas = Canvas(frame, width, height)
        return (frame, canvas)

    def _create_control_frame(self):
        control_frame = Tkinter.Frame(self._frame)
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

        frame = self._create_frame(canvas_width, canvas_height, control_width)
        self._frame = frame

        (frame, canvas) = self._create_canvas(canvas_width, canvas_height)
        self._canvas_frame = frame
        self._canvas = canvas

        self._control_frame = self._create_control_frame()
        self._controls = []

        (stats, keys, mouse) = self._create_status_frame()
        self._stats_frame = stats
        self._key_frame = keys
        self._mouse_frame = mouse

    def _shutdown(self):
        self._canvas.destroy()
        self._root.destroy()

    def start(self):
        self._root.mainloop()

    def set_draw_handler(self, draw_handler):
        self._canvas.set_draw_handler(draw_handler)

    def add_button(self, text, button_handler, width=None):
        button = Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)

    def add_label(self, text):
        label = Tkinter.Label(self._control_frame, text=text)
        self._controls.append(label)


def create_frame(title, canvas_width, canvas_height, control_width=200):
    return Frame(title, canvas_width, canvas_height, control_width)
