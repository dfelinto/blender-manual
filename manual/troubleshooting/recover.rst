
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

The *File* tab of the *Preferences* allows you to configure the two ways
that Blender provides for you to regress to a previous version of your work.
See :ref:`Auto Save Preferences <prefs-auto-save>` for details.


.. _troubleshooting-file-recovery:

Recovering Auto Saves
=====================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`File --> Recover --> Last Session`
   :Menu:      :menuselection:`File --> Recover --> Auto Save...`


Recover Last Session
--------------------

The *Recover Last Session* will open the ``quit.blend`` file
that is saved into the :ref:`temp-dir` when you quit Blender under normal operation.
Note that files in your temporary directory may be deleted when you reboot your computer
(depending on your system configuration).


Recover Auto Save
-----------------

The *Recover Auto Save* allows you to open the *Auto Saved* file.
You will have to navigate to your :ref:`temp-dir`.
The *Auto Saved* files are named using a random number and have a blend extension.

It is important, when browsing, to enable the detailed list view.
Otherwise, you will not be able to figure out the dates of the auto-saved blend-files.
See Fig. :ref:`fig-troubleshooting-file-browser`.

.. _fig-troubleshooting-file-browser:

.. figure:: /images/troubleshooting_recover_display-file-date.png

   File Browser displaying a vertical list.

.. warning::

   When recovering an *Auto Saved* file, you will lose any changes made
   since the last *Auto Save* was performed.
   Only one *Auto Saved* file exists for each project,
   i.e. Blender does not keep older versions.
   Hence, you will not be able to go back more than a few minutes with this tool.
