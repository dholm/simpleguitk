# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from string import hexdigits


ColorMap = {'Aqua': '#00ffff',
            'Black': '#000000',
            'Blue': '#0000ff',
            'Fuchsia': '#ff00ff',
            'Gray': '#808080',
            'Green': '#008000',
            'Lime': '#00ff00',
            'Maroon': '#800000',
            'Navy': '#000080',
            'Olive': '#808000',
            'Purple': '#800080',
            'Red': '#ff0000',
            'Silver': '#c0c0c0',
            'Teal': '#008080',
            'White': '#ffffff',
            'Yellow': '#ffff00'}


def map_color(color):
    if color is None:
        return None
    elif color in ColorMap:
        return ColorMap[color]
    elif all(c in hexdigits for c in color):
        return '#%s' % color
    return color
