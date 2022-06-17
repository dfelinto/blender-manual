
************
Introduction
************

Here are some preferences that you may wish to set initially.
See the section :doc:`Preferences </editors/preferences/index>`
for the complete list of available settings.


Language
========

Enable :menuselection:`Edit --> Interface --> Translation`,
and choose the *Language* and what to translate from *Interface*, *Tooltips* and *New Data*.

See :ref:`prefs-interface-translation` for details.


Input
=====

If you have a compact keyboard without a separate number pad, enable
:menuselection:`Preferences --> Input --> Keyboard --> Emulate Numpad`.

If you do not have a middle mouse button, you can enable
:menuselection:`Preferences --> Input --> Mouse --> Emulate 3 Button Mouse`.

See :doc:`Input Preferences </editors/preferences/input>` for details.


File and Paths
==============

At :menuselection:`Preferences --> File Paths`
you can set options such as what *Image Editor* (GIMP, Krita...)
and *Animation Player* to use.

The :ref:`temp-dir` sets where to store files such as temporary renders and auto-saves.

.. tip::

   The ``//`` at the start of each path in Blender means the directory of the currently opened blend-file,
   used to reference relative paths.

See :doc:`File Preferences </editors/preferences/file_paths>` for details.


Save & Load
===========

If you trust the source of your blend-files, you can enable *Auto Run Python Scripts*.
This option is meant to protect you from malicious Python scripts in blend-files that you got from someone else.
Many users turn this option on, as advanced rigs tend to use scripts of some sort.

See Save & Load :ref:`prefs-auto-execution` Preference.
