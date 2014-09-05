
..    TODO/Review: {{review}} .

Recovering from mistakes or problems
************************************

Blender provides a number of ways for the user to recover from mistakes,
and reduce the chance of losing their work in the event of operation errors,
computer failures, or power outages.
There are two ways for you to recover from mistakes or problems:

At the :ref:`User Level <options-for-actions>` (Relating to :guilabel:`Actions`)

- For your actions, there are options like :guilabel:`Undo`, :guilabel:`Redo` and an :guilabel:`Undo History`,
  used to roll back from mistakes under normal operation, or return back to a specific action.
- Blender also has new features like :guilabel:`Repeat` and :guilabel:`Repeat History`,
  and the new :guilabel:`Redo Last` which you can use in conjunction with the options listed.

At the :ref:`System Level <options-for-files>` (Relating to :guilabel:`Files`)

- There are options to save your files like
  :guilabel:`Auto Save` that saves your file automatically over time, and :guilabel:`Save on Quit`,
  which saves your Blender file automatically when you exit Blender.
  Note: In addition to these functions being enabled by default,
  the :guilabel:`Save on Quit` functionality cannot be disabled.


.. _options-for-actions:

Options for Actions (User Level)
================================

.. figure:: /images/Manual-Vitals-Undo-and-Redo-UndoOptions.jpg

   Undo options


The commands listed below will let you roll back an accidental action, redo your last action,
or let you choose to recover to a specific point,
by picking from a list of recent actions recorded by Blender. Two new features that were added
to the Blender 2.5x series are the :guilabel:`Repeat` and :guilabel:`Repeat History` commands.

To enable or disable Undo,
go to the :guilabel:`User Preferences` window and click on the :guilabel:`Editing` tab.
In this section you can set:

Global Undo
   This enables Blender to save actions done when you are **not** in :guilabel:`Edit Mode`.
   For example, duplicating Objects, changing panel settings or switching between modes.
   The default Blender Installation comes with the option *Global Undo* enabled.

Steps
   This numeric field indicates how many steps or actions to save.
   The default value of **32** will allow you to Undo the last thirty-two actions that you performed.
   You can change this numeric field to the maximum of **64**.

Memory Limit
   This numeric field allows you to define the maximum amount of memory in Megabytes
   that the Undo system is allowed to use. The default value of **0** indicates no limit.


Undo
----

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`ctrl-Z`


Like most programs, if you want to undo your last action, just press :kbd:`ctrl-Z`

Redo
----

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`shift-ctrl-Z`


To roll back your Undo action, press :kbd:`shift-ctrl-Z`

Redo Last
---------

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`F6`


Redo Last (New feature) is short for :guilabel:`Redo(ing your) Last (Action)`. Hitting
:kbd:`F6` after an action will present you a context-sensitive Pop-Up Window based on
your last action taken and the :guilabel:`Mode` and :guilabel:`Window` in which Blender is
being used.

For example, if your last action was a rotation in :guilabel:`Object` Mode,
the Window will show you the last value changed for the angle (see Fig:Redo Last - Rotation),
where you can change your action back completely by typing **0** (zero)
in the numeric field. There are other useful options, based on your action context,
and you can not only Undo actions, but change them completely using the available options.

If you are in :guilabel:`Edit` Mode,
the Window will also change its contents based on your last action taken.
In our second example (at the right), the last action taken was a Vertex Move;
we did a :guilabel:`Scale` on a Face, and, as you can see,
the contents of the Pop-Up Window are different, because of your context (Edit Mode).
(See Fig:Redo Last - Scale)


.. figure:: /images/Manual-Vitals-Undo-Redo-F6-Rotation-Object-Edit.jpg

   Redo Last - Rotation ( Object Mode, 60 degrees ) _________ Redo Last - Scale ( Edit Mode, Resize face )


.. tip:: Operations using Redo Last

   Some operations produce particularly useful results if you tweak their parameters with the :kbd:`F6` Menu. Take, for example, adding a Circle. If you reduce the Vertex count to 3, you get a perfect equilateral triangle.


Undo History
------------

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`Ctrl-Alt-Z`


.. figure:: /images/Manual-Vitals-Undo-Redo-Ctrl+Alt+z_Menu.jpg

   The Undo History menu, which appears upon [Ctrl][Alt][z] press.


There is also a Undo History of your actions, recorded by Blender.
You can access the history with :kbd:`ctrl-alt-Z`.

Rolling back actions using the *Undo History* feature will take you back to the action you
choose. Much like how you can alternate between going backward in time with
:kbd:`Ctrl-z` and then forward with :kbd:`Shift-Ctrl-z`, you can hop around on the
Undo timeline as much as you want as long as you do not make a new change.
Once you do make a new change, the Undo History is truncated at that point.


Repeat Last
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`shift-r`


The Repeat Last feature will Repeat your last action when you press :kbd:`shift-r`.

In the example Images below, we duplicated a *Monkey* :guilabel:`Mesh`,
and then we moved the Object a bit. Using repeat :kbd:`Shift-r`,
the *Monkey* was also duplicated and moved.


+------------------------------------------+------------------------------------------+------------------------------------------+
+.. figure:: /images/UndoRedo-00.Repeat.jpg|.. figure:: /images/UndoRedo-01.Repeat.jpg|.. figure:: /images/UndoRedo-02.Repeat.jpg+
+                                          |                                          |                                          +
+   Suzanne.                               |   After a [Shift][d] and move.           |   After a [Shift][r].                    +
+------------------------------------------+------------------------------------------+------------------------------------------+


Repeat History
--------------

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`F3`


.. figure:: /images/Manual-Vitals-Undo-Redo-F3_Menu.jpg

   The Repeat menu, which appears upon [F3] press.


The (New feature) Repeat History will present you a list of the last repeated actions,
and you can choose the actions you want to repeat.
It works in the same way as the Undo History, explained above,
but the list contains only repeated actions.  To access Repeat History, use :kbd:`F3`.


.. note:: There are two separate Histories for Blender

   Blender uses two separate Histories, one dedicated for the :guilabel:`Edit` Mode,
   and one dedicated for the :guilabel:`Object` Mode.


Blender Search
--------------

.. figure:: /images/Manual-Vitals-Undo-Redo-Redo_Last_Spacebar_Menu.jpg

   Spacebar search for Redo Last


You can always access all of the explained options for user actions,
using Blender Search :kbd:`Space`.


.. important::

   When you quit Blender, the complete list of user actions will be lost, even if you save your file before quitting.


.. _options-for-files:

Options for Files (System Level)
================================

Save and Auto Save
------------------

.. figure:: /images/Manual-Vitals-Undo-and-Redo-AutosaveOptions.jpg

   Auto Save options


Computer crashes,
power outages or simply forgetting to save can result in the loss or corruption of your work.
To reduce the chance of losing files when those events occur,
Blender can use an :guilabel:`Autosave` function. The :guilabel:`File` tab of the
:guilabel:`User Preferences` window allows you to configure the two ways that Blender provides
for you to regress to a previous version of your work.

Save on Quit
   The function :guilabel:`Save on Quit` is enabled by default in Blender.
   Blender will always save your files when you quit the application under normal operation.

Save Versions
   This option tells Blender to keep the indicated number of saved versions of your file in your current working
   directory when you manually save a file. These files will have the extension: ``.blend1``, ``.blend2``, etc.,
   with the number increasing to the number of versions you specify. Older files will be named with a higher number.
   e.g. With the default setting of **2**, you will have three versions of your file: ``*.blend`` (your last save),
   ``*.blend1`` (your second last save) and ``*.blend2`` (your third last save).


Auto Save Temporary Files
   Checking this box tells Blender to *automatically* save a backup copy of your work-in-progress to the Temp
   directory (refer to the :guilabel:`File` panel in the :guilabel:`User Preferences` window for its location).
   This will also enable the :guilabel:`Timer
   (mins)` control which specifies the number of minutes between each Auto Save.
   The default value of the Blender installation is **5** (5 minutes). The minimum is **1**,
   and the Maximum is **60**
   (Save at every one hour).The Auto Saved files are named using a random number and have a ``.blend`` extension.



.. tip:: Compress Files

   The option to Compress files will try to compact your files whenever Blender is saving them. Large Scenes,
   dense Meshes, big Textures or lots of elements in your Scene will result in a big ``.blend`` being created.
   This option could slow down Blender when you quit,
   or under normal operation when Blender is saving your backup files. In fact,
   using this option you will trade processor time for file space.



Recovering Auto Saves
---------------------

Recover Last Session
   :menuselection:`File --> Recover Last Session` will open the ``quit.blend``
   that is saved into the :guilabel:`Temp` directory when you exit Blender.
   Note that files in your :guilabel:`Temp` directory are deleted when you reboot.


.. figure:: /images/Manual-Vitals-Undo-Display_File_Date.jpg

   Blender File Browser


.. tip::

   When recovering files, you will navigate to your temporary folder.
   It is important, when browsing, to enable the detailed list view.
   Otherwise, you will not be able to figure out the dates of the auto-saved .blends.
   (See Figure: Blender File Browser)


Recover Auto Save
   :menuselection:`File --> Recover Auto Save...` allows you to open the Auto Saved file.
   After loading the Auto Saved version,
   you may save it over the current file in your working directory as a normal ``.blend`` file.


.. important::

   When recovering an Auto Saved file, you will lose any changes made since the last :guilabel:`Auto Save` was
   performed.Only **one** Auto Saved file exists for each project
   (i.e. Blender does not keep older versions -
   hence you won't be able to go back more than a few minutes with this tool).



Other options
-------------

Recent Files
   This setting controls how many recent files are listed in the :menuselection:`File --> Open Recent` sub-menu.

Save Preview Images
   Previews of images and materials in the :guilabel:`File Browser` window are created on demand.
   To save these previews into your ``.blend`` file, enable this option
   (at the cost of increasing the size of your .blend file).

