.. -*- restructuredtext -*-

===========
SimpleGUITk
===========

**SimpleGUITk** is a wrapper for the `CodeSkulptor
<http://www.codeskulptor.org/>`_ *SimpleGUI* API using *TkInter*.
*CodeSkulptor* is a browser-based Python interpreter used in the online
course "`An Introduction to Interactive Programming in Python
<https://www.coursera.org/course/interactivepython>`_".


This wrapper makes it easier to work in the development environment of your
choice while still being able to quickly test your implementation without using
a web browser.


Requirements
============

 * `Pillow <https://github.com/python-imaging/Pillow>`_ in order to use images.
 * `Pygame <http://www.pygame.org/>`_ for sound support.

None of these are strict requirements as SimpleGUITk will run without them as
long as you don't need to use the *SimpleGUI Images* or *SimpleGUI Sounds*
APIs.


Usage
=====

The most practical way to use SimpleGUITk is to use the following import
statement which makes it easy to switch between SimpleGUI and SimpleGUITk.

    import simpleguitk as simplegui

Assuming you intend to eventually run your code in CodeSkulptor make it a habit
to test it often. As of this writing some of Python's language features are
unavailable in CodeSkulptor and catching these early on makes it easier to make
sure your implementation works as expected.


Changes
=======

- **1.1.0**

  * Initial support for SimplePlot via matplotlib.
  * Support for Python 3.
  * Fixes size issues with control objects.


- **1.0.6**

  * Moves SimpleGUITk version to base directory to avoid dependency cycle during
    installation.


- **1.0.5**

  * Ensure canvas refresh is within a reasonable interval.


- **1.0.4**

  * Canvas borderes will now render correctly.
  * The draw handler uses an adaptive timeout so that it will run smoothly at
    60 FPS just like in CodeSkulptor.
  * Polygons default fill set to transparent.


- **1.0.3**

  * Prevent the input status labels from resizing dynamically which would cause
    the canvas to move around on certain events.
  * Increase of FPS to 100 to better match SimpleGUI in CodeSkulptor.


- **1.0.2**

  * Display input events in the status frame.
  * Ignore case on color codes when using named colors.
  * Input control events are sent as strings like in SimpleGUI.
  * Several minor bugfixes


- **1.0.1**

  * Translation of TkInter keys to JavaScript keycodes so they will work with
    implementations that do not use *simplegui.KEY_MAP*.
  * Support for colors specified as hexadecimal without a leading hash sign.
  * Bugfixes for older versions of TkInter.


- **1.0.0**

  * First official release.
