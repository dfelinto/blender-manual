
***************
Recovering Data
***************

Computer crashes, power outages, or simply forgetting to save can result in
the loss or corruption of your work. You can use Blender's *Auto Save* feature
to reduce the chance of losing files when such events occur.

There are options to save a backup of your files like
*Auto Save* that saves your file automatically over time, and *Save on Quit*,
which saves your blend-file automatically when you exit Blender.
In addition to these functions being enabled by default,
the *Save on Quit* functionality cannot be disabled.

.. note::

   For your actions, there are options like *Undo*, *Redo* and an *Undo History*,
   used to roll back from mistakes under normal operation, or return back to a specific action.
   See :doc:`/interface/undo_redo`.


.. _troubleshooting-file_recovery-save_versions:

Recovering Save Versions
========================

By default Blender keeps an additional backup when saving files.
So saving renames the previously saved file with a ``.blend1`` extension instead of overwriting it.

This file can be used to revert to a previous state.

See :ref:`Save Versions <prefs-save_load-backups>` to configure the number of versions kept.


.. _troubleshooting-file_recovery-auto_save:

Recovering Auto Saves
=====================

Last Session
------------

.. reference::

   :Menu:      :menuselection:`File --> Recover --> Last Session`

The *Recover Last Session* will open the ``quit.blend`` file
that is saved into the :ref:`temp-dir` when you quit Blender under normal operation.
Note that files in your temporary directory may be deleted when you reboot your computer
(depending on your system configuration).


Auto Save
---------

.. reference::

   :Menu:      :menuselection:`File --> Recover --> Auto Save`

The *Recover Auto Save* allows you to open the *Auto Saved* file.
You will have to navigate to your :ref:`temp-dir`.
The *Auto Saved* files are named using a random number and have a blend extension.

See :ref:`Auto Save Preferences <prefs-auto-save>` to configure auto-save.

Trusted Source
   When enabled, Python scripts and drivers that may be included in the file will be run automatically.
   Enable this only if you created the file yourself,
   or you trust that the person who gave it to you did not include any malicious code with it.
   See :doc:`Python Security </advanced/scripting/security>` to configure default trust options.

.. tip::

   Enable the detailed list view when browsing auto-saved files to show which is the most recent.

   .. figure:: /images/troubleshooting_recover_display-file-date.png

      File Browser displaying a vertical list.

.. warning::

   When recovering an *Auto Saved* file, any changes made since the last *Auto Save* will be lost.
   Only one *Auto Saved* file exists for each ``.blend`` file, i.e. Blender does not keep older versions.
   Therefor, you will only be able to restore the most recent *Auto Save* file.
