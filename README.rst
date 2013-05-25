.. -*- restructuredtext -*-

SimpleGUITk
===========

SimpleGUITk is a wrapper for the `CodeSkulptor <http://www.codeskulptor.org/>`_
SimpleGUI API using TkInter. CodeSkulptor is a browser-based Python interpreter
used in the online course "`An Introduction to Interactive Programming in
Python <https://www.coursera.org/course/interactivepython>`_".


This wrapper makes it easier to work in the development environment of your
choice while still being able to quickly test your implementation without using
a web browser.


Requirements
------------

 * `Pillow <https://github.com/python-imaging/Pillow>`_ 2.0.0 in order to use
   images.
 * `Pygame <http://www.pygame.org/>`_ 1.9.0 for sound support.


Usage
-----

The most practical way to use SimpleGUITk is to use the following import
statement which makes it easy to switch between SimpleGUI and SimpleGUITk.

    import simpleguitk as simplegui

Assuming you intend to eventually run your code in CodeSkulptor make it a habit
to test it often. As of this writing some of Python's language features are
unavailable in CodeSkulptor and catching these early on makes it easier to make
sure your implementation works as expected.
