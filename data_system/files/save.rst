
Saving Files
============

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`File --> Save`
   | Hotkey:   :kbd:`F2`


Description
===========

Saving files is like loading files. When you press :kbd:`F2`, :guilabel:`File Browser` window will open.
The window appears the same as when opening files, except for a few options in the side panel.
For descriptions and usage of the file browser functions,
see the page on :doc:`Opening files <data_system/files/open>`.


.. figure:: /images/File-savewindow.jpg


Saving
======

Click the lower edit box to enter a filename. If it doesn't end with "\ ``.blend`` ",
the extension is automatically appended.
Then press :kbd:`enter` or click the :guilabel:`Save File` button to save the file.

When saving via menu or pressing :kbd:`F2`,
:kbd:`ctrl-shift-s` or :kbd:`ctrl-alt-s`,
if a file with the same given name already exists, the edit box will turn red as a warning,
if you press Enter or the Save button,
it will automatically save over the existing file with the same name. So,
think twice before you continue saving.

By default, when pressing :kbd:`ctrl-s` or :kbd:`ctrl-W`,
it will pop-up a message for you to confirm your saving,
which aims to avoid the "accidental" saving operation, which may not be what you want. (e.g.
say, you want to press Ctrl A when operating, but the Ctrl S is pressed,
then you can just move your mouse cursor out of the pop-up,
the accidental saving operation will be canceled.)

Depending on the number of :doc:`Save Versions <vitals/undo_and_redo#save_and_auto_save>` you have set, all existing files with the same name will be rotated to a ``.blend`` *n* file extension, where *n* is ``1``, ``2``, ``3``, etc. So, if you were working on ``MyWork.blend``, and saved it, the existing ``MyWork.blend`` is renamed to ``MyWork.blend1``, and a new ``MyWork.blend`` is saved. This way, you have hot backups of old saved versions that you can open if you need to massively undo changes.


Save Options
============

The save options appear at the bottom of the side panel.


Compress File
-------------

Enable this option to squash large files, this removes dead space.


Remap Relative
--------------

This option remaps relative paths when saving a file in a new location


Save Copy
---------

This option saves a copy of the actual working state, but does not make the saved file active.


Tip for Save Increments
-----------------------

The save dialog contains a little feature to help you to create multiple versions of your
work: pressing :kbd:`pad+` or :kbd:`pad-` increments or decrements a number at the
end of the file name. To simply save over the currently loaded file and skip the save dialog,
press :kbd:`ctrl-W` instead of :kbd:`F2` and just confirm at the prompt.


