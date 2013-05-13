import threading


class Timer(object):
    def __init__(self, interval, timer_handler):
        self._interval = interval
        self._timer = None
        self._timer_handler = timer_handler
        self._running = False

    def _schedule(self):
        if self._running:
            interval = self._interval / 1000.0
            self._timer = threading.Timer(interval, self._handler)
            self._timer.start()

    def _handler(self):
        self._timer_handler()
        self._schedule()

    def start(self):
        self._running = True
        self._schedule()

    def stop(self):
        self._running = False
        self._timer.cancel()

    def is_running(self):
        return self._running


def create_timer(interval, timer_handler):
    return Timer(interval, timer_handler)
