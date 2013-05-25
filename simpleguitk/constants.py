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


def map_color(c):
    if c is None:
        return None
    elif c in ColorMap:
        return ColorMap[c]
    return c
