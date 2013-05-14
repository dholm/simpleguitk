import Tkinter

from .timers import create_timer


class Canvas(object):
    IntervalMs = 125

    def __init__(self, master, width, height):
        self._canvas = Tkinter.Canvas(master, width=width, height=height)
        self._canvas.grid(row=0, column=1, rowspan=2)

        self._draw_handler_fn = None
        self._draw_handler_timer = None

    def _draw_handler(self):
        if self._draw_handler is not None:
            self._canvas.delete('all')
            self._draw_handler_fn(self)

    def destroy(self):
        self._draw_handler_timer.stop()

    def set_draw_handler(self, draw_handler):
        self._draw_handler_fn = draw_handler
        self._draw_handler_timer = create_timer(Canvas.IntervalMs,
                                                self._draw_handler)
        self._draw_handler_timer.start()

    def draw_text(self, text, point, font_size, font_color, font_face='serif'):
        self._canvas.create_text(point, text=text, fill=font_color,
                                 font=(font_face, font_size))
