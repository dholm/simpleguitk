# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

VERSION = (1, 1, 3)
__version__ = ''.join(['-.' [type(x) == int] + str(x) for x in VERSION])[1:]
