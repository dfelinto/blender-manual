.. _linux-windowing-environment:

*********************
Windowing Environment
*********************

On Linux Blender supports both X11 and Wayland for official releases.

When Wayland is detected, is is the preferred system, otherwise X11 will be used.

.. hint::

   The current "Windowing Environment" is listed in :menuselection:`File --> About`.


X11
===

This is the windowing environment that has been used most widely on Linux & Unix systems.

There are no near-term plans to deprecate or remove X11 support.


Wayland
=======

Support for Wayland is a more recent addition, so there may be configurations that have not been tested yet.
Please report a bug if you experience problems.

Blender has been tested with Gnome-Shell (mutter), KDE (plasma) & SWAY (wlroots) based compositors.


Requirements
------------

Gnome-Shell
   Under Gnome-Shell the ``libdecor`` library is required.
   This is available as a package on most Linux distribution.

   If the library isn't found X11 will be used as a fallback.


Troubleshooting
---------------

Detailed Wayland output can help to track down problems.
Launch Blender from the :doc:`command-line </advanced/command_line/launch/linux>` with additional arguments:

Blender's Wayland Logging
   .. code-block:: sh

      blender --log "ghost.wl.*" --log-level 2

Wayland Built-In Logging
   .. code-block:: sh

      WAYLAND_DEBUG=1 blender


Known Limitations
-----------------

NVidia GPU
   Currently NVidia drivers don't fully support features needed for Wayland support,
   graphical glitches and flickering is a common problem, this is not specific to Blender
   so NVidia users may want to use X11 until driver support improves.

----

Feature Comparison
==================

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 30 5 5 60

   * - Feature
     - X11
     - Wayland
     - Notes
   * - Smooth Scroll
     - |cross|
     - |tick|
     - | Smooth scrolling with track-pads.
   * - Multi-Touch Gestures
     - |cross|
     - |tick|
     - | Track-pad and tablet support for
       | pinch to zoom, pan and orbit.
   * - Reliable Cursor Warping
     - |cross| :sup:`*1`
     - |tick|
     - | Track-pad and tablet support for
       | pinch to zoom, pan and orbit.
   * - Window Positioning
     - |tick|
     - |cross| :sup:`*2`
     - | Needed for dragging between windows and
       | restoring window positions on file load.
   * - Window Raise/Lower
     - |tick|
     - |cross| :sup:`*2`
     - | Used to bring the render window
       | to the foreground.

Other features which both systems support such as Hi-DPI, 3D-mouse, tablet input, ... etc.
have been left out of this list.

| :sup:`*1` In X11 fast cursor motion may exit the window bounds while the cursor is grabbed (transforming for e.g.).
| :sup:`*2` Wayland doesn't support setting the window position & depth,
  as this is a design decision it's unlikely to be supported (see issues for
  `position <https://developer.blender.org/T98928>`__ and
  `depth <https://developer.blender.org/T102985>`__).
