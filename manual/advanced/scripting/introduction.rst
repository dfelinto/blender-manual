
************
Introduction
************

Python is an interpreted, interactive, object-oriented programming language.
It incorporates modules, exceptions, dynamic typing, very high-level dynamic data types, and classes.
Python combines remarkable power with very clear syntax.

Python scripts are a versatile way to extend Blender functionality.
Most areas of Blender can be scripted, including animation, rendering, import and export,
object creation and automating repetitive tasks.

To interact with Blender, scripts can make use of
the tightly integrated :abbr:`API (Application Programming Interface)`.


General Information
===================

Links that are useful while writing scripts:

- `Python.org <https://www.python.org/>`__
  -- General information about Python.
- `Blender Python API <https://docs.blender.org/api/current/>`__
  -- Official API documentation. Use this for referencing while writing scripts.
- `API Introduction <https://docs.blender.org/api/current/info_quickstart.html>`__
  -- A short introduction to get you started with the API. Contains examples.

Links that deal with distributing your scripts:

- `Sharing scripts <https://wiki.blender.org/wiki/Process/Addons>`__
  -- Information on how to share your scripts and get them included in the official Blender distribution.
- `Creating Add-ons <https://wiki.blender.org/wiki/Process/Addons/Guidelines>`__
  -- Add-ons are used to encapsulate and distribute scripts.
- `Add-ons project <https://developer.blender.org/project/profile/3/>`__
  -- Project to maintain a central repository of extensions to Blender.


Getting Started
===============

.. rubric:: Manual links

The following links take you from the basics to the more advanced
concepts of Python scripting for Blender.

- :doc:`Text Editor </editors/text_editor>`
- :doc:`Python Console </editors/python_console>`
- :doc:`Info Editor </editors/info_editor>`


.. rubric:: External links

Here are external links containing a lot of good information
to start learning how to write scripts for Blender:

- `Python API: Quickstart <https://docs.blender.org/api/current/info_quickstart.html>`__
- `CG Cookie: Blender 2.8 Python Scripting Superpowers for Non-Programmers
  <https://cgcookie.com/articles/blender-2-8-python-scripting-superpowers-for-non-programmers>`__
- `Olav3D Tutorials: 3D Programming for Beginners Using Python
  <https://www.youtube.com/watch?v=rHzf3Dku_cE>`__
- `Blender Artists: Python Support Forum <https://blenderartists.org/c/coding/python-support>`__


Extending Blender
=================

Add-ons
-------

Add-ons are scripts that enable Blender to gain extra functionality;
they can be enabled from the :doc:`Preferences </editors/preferences/addons>`.

Outside of the Blender executable, there are hundreds of add-ons written by many people:

- Officially supported add-ons are bundled with Blender.
- Other *Testing* add-ons are included in `development builds <https://builder.blender.org/download/>`__
  of Blender but not official releases.
  Many of them work reliably and are very useful but are not yet ensured to be stable for release.

.. seealso::

   See :doc:`/addons/index` for documentation on add-ons included with Blender.


Scripts
-------

Apart from add-ons, there are several other types of scripts that extend Blender's functionality:

:Modules:
   Utility libraries for import into other scripts.
:Presets:
   Settings for Blender's tools and key configurations.
:Startup:
   These files are imported when starting Blender.
   They define most of Blender's UI, as well as some additional core operators.
:Custom Scripts:
   In contrast to add-ons, they are typically intended for one-time execution via
   the :doc:`Text Editor </editors/text_editor>`.


Saving your own Scripts
-----------------------

File Location
^^^^^^^^^^^^^

All scripts are loaded from the ``scripts`` folder of
the :ref:`local, system and user paths <blender-directory-layout>`.

You can setup an additional search path for scripts in
:ref:`prefs-file-paths` :menuselection:`Preferences --> File Paths`.


Installation
^^^^^^^^^^^^

Add-ons are conveniently installed through Blender in the :doc:`Preferences </editors/preferences/addons>`.
Click the :menuselection:`Install...` button and select the ``.py`` or ``.zip`` file.

To manually install scripts or add-ons, place them in the ``addons``, ``modules``, ``presets``,
or ``startup`` directory according to their type. See the description above.

You can also run scripts by loading them in the :doc:`Text Editor </editors/text_editor>`.
