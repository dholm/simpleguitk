# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

try:
    import matplotlib.pyplot
except ImportError:
    print('matplotlib must be installed in order to use SimplePlot!')
    raise


def plot_lines(framename, width, height, xlabel, ylabel, datasets,
               points=False, legends=None):
    matplotlib.pyplot.title(framename)
    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)
    marker = None
    if points:
        marker = 'o'
    for i in range(len(datasets)):
        label = ''
        if i < len(legends):
            label = legends[i]

        (xdata, ydata) = ([], [])
        if type(datasets[i]) is dict:
            for x, y in sorted(datasets[i].items()):
                xdata.append(x)
                ydata.append(y)

        elif type(datasets[i]) is list:
            for x, y in datasets[i]:
                xdata.append(x)
                ydata.append(y)

        else:
            raise TypeError('Type %s currently unsupported' %
                            type(datasets[i]))

        matplotlib.pyplot.plot(xdata, ydata, label=label, marker=marker)
    if len(legends):
        matplotlib.pyplot.legend(loc='upper right')
    matplotlib.pyplot.show()
