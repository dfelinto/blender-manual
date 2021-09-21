
************
File Browser
************

The File Browser is used in all the file-related operations. These include:

- Opening and saving blend-files.
- Browsing inside other blend-files, when appending or linking data-blocks,
  see :doc:`Linked Libraries </files/linked_libraries/index>`.
- Importing from/exporting to other file formats.
- Picking new locations for existing file paths (images, videos, fonts...).

The most common way to use this editor is through modal operators (like opening or saving a blend-file).
It will appear maximized, waiting for the operation to complete,
and then close and return to the former screen layout.

.. note::

   You can always select several entries in the File Browser,
   the last selected one is considered as the active one.
   If the calling operation expects a single path (like e.g. the main blend-file *Open* one),
   it will get that active item's path, other selected ones will just be ignored.

You can also keep the File Browser open, as any other editor type, to browse through the file system.
The main purpose of this is to be able to drag-and-drop media files:

- Images into the :ref:`editors-3dview-index` (to set as background or apply as material texture).
- Media files into the :ref:`editors-sequencer-index`.

.. figure:: /images/editors_file-browser_editor.png

   The File Browser.


Header
======

View Menu
---------

Select
------


File Path
=========

.. _bpy.ops.file.previous:

Previous Folder :kbd:`Backspace`, :kbd:`Alt-Left`
   Move to previous folder (in navigation history).

.. _bpy.ops.file.next:

Next Folder :kbd:`Shift-Backspace`, :kbd:`Alt-Right`
   Move to next folder (in navigation history).

.. _bpy.ops.file.parent:

Parent File :kbd:`P`, :kbd:`Alt-Up`
   Move up to parent directory.

.. _bpy.ops.file.refresh:

Refresh File List :kbd:`R`, :kbd:`NumpadPeriod`
   Refresh current folder.

.. _bpy.ops.file.directory_new:

Create Directory :kbd:`I`
   Will ask you to confirm and create a new directory inside current one,
   scroll to it in the main view, and let you enter its name.

.. _bpy.types.FileSelectParams.directory:

File Path
   Text field for the current folder path.
   :kbd:`Tab` will auto-complete an existing path.
   If you type a nonexistent directory path, you will be prompted to create that new directory.

.. _bpy.types.FileSelectParams.filter_search:

Search :kbd:`Ctrl-F`
   Filter items by name.
   The wildcard ``*`` will match anything, e.g. ``bl*er`` will match both ``blender`` and ``blogger``.
   There is always an implicit wildcard at start and end of the search text,
   so ``blender`` will also match ``test_blender_file.blend``.
   This field can also be used to filter some specific file extension (e.g. ``.png`` will list all PNG files).

.. _bpy.types.FileSelectParams.display_type:

Display Mode
   Controls how files are displayed.

   :Vertical List: Displays files and folders in a vertical list.
   :Horizontal List: Displays files and folders in a horizontal list.
   :Thumbnails: Shows :ref:`previews <file_browser-previews>`.



Display Settings
----------------

.. _bpy.types.FileSelectParams.display_size:

Display Size
   The size of the thumbnails, or the width of the columns.

.. _bpy.types.FileSelectParams.recursion_level:

Recursion
   The number of directory levels to show at once in a flat way.

   :None: List only the current directory content.
   :Blend File: List the whole content of a blend-file (only available when linking or appending data-blocks).
   :One Levels: List all sub-directories’ content, one level of recursion.
   :Two Levels: List all sub-directories’ content, two level of recursion.
   :Three Levels: List all sub-directories’ content, three levels of recursion

   .. hint::

      Showing several levels of directories at once can be handy to e.g. see your whole collection of textures,
      even if you have arranged them in a nice set of directories to avoid having hundreds of
      files in a single place.

      In the *Append/Link* case, showing the content of the whole blend-file will allow you
      to link different types of data-blocks in a single operation.

   .. warning::

      The more levels you show at once, the more time it will take to list them all
      (typically, it will be exponential, showing three levels at once
      may take three orders of magnitude more time to be fully listed).

.. _bpy.types.FileSelectParams.sort_method:

Sort By
   Sorts items by one of the four methods:

   :Name: Sort the file list alphabetically.
   :Extension: Sort the file list by extension/type.
   :Modified Date: Sort files by modification time.
   :Size: Sort files by size.


.. _bpy.types.FileSelectParams.use_filter:

Filter Settings
---------------

On the right side of the file path are the filtering options.
The first "funnel" button controls whether filtering is enabled or not.

File Types
   Filters files by categories, like folders, blend-files, images, etc.

.. _bpy.types.FileSelectIDFilter:

Blender IDs
   When appending or linking, you can also filter by data-block categories, like scenes, animations, materials, etc.

.. _bpy.types.FileSelectParams.show_hidden:

Show Hidden :kbd:`H`
   Shows hidden files (starting with a ``.``).


File Name & Execution
=====================

.. _bpy.types.FileSelectParams.filename:

File Name
   Text field to edit the file name and extension.
   When saving, if the background is red, a file with same name already exists in the folder.
   :kbd:`Tab` will auto-complete to existing names in the current directory.

   Increment Filename ``-``, ``+``
      Removes/Decreases or adds/increases a trailing number to your file name
      (used e.g. to store different versions of a file).

.. _bpy.ops.file.cancel:

Cancel :kbd:`Esc`
   Cancels the file selection (and the underlying operation), and closes the File Browser.
   Using the *Back to Previous* button in the :doc:`Topbar </interface/window_system/topbar>`
   will have the same effect.

.. _bpy.ops.file.execute:

Confirm :kbd:`Return`
   The main button to validate the operation, which defines its name.
   Double-clicking on a non-directory item will have the same effect.


Source List
===========

The left region displays different ways to quickly access some directories.
The region is divided into separate panels each containing a :ref:`UI List <ui-list-view>` of directories.
Clicking on one of the directories will immediately navigate to that folder.


.. _bpy.types.SpaceFileBrowser.system_folders:

Volumes
-------

Contains all OS-defined available volumes, e.g. drives or network mounts.


.. _bpy.types.SpaceFileBrowser.system_bookmarks:

System
------

Contains OS-defined common directories, like the main user folder...


.. _bpy.types.SpaceFileBrowser.bookmarks:

Bookmarks
---------

Contains folders that you want to be able to access often without having to navigate to them in the File Browser.
To the right of that list are buttons to perform basic management actions on your bookmarks,
e.g. add/remove an entry, move it up or down in the list, etc.


.. _bpy.types.SpaceFileBrowser.recent_folders:

Recent
------

Contains recently accessed folders.

.. _bpy.ops.file.reset_recent:

The ``X`` button to the right allows you to fully erase this list.

You can control how many folders appear in this list with the *Recent Files* number field
of the :ref:`Save & Load <prefs-save-load>` tab in the Preferences.


Operator Options
================

The right region shows the options of the calling operator.
Besides common actions listed below, many import/export add-ons will also expose their options there.

Open, Save, Save As Blender File
   See :doc:`/files/blend/open_save`.
Open, Replace, Save As Image
   See :doc:`/files/media/image_formats`.
Link/Append from Library
   See :doc:`Linked libraries </files/linked_libraries/index>`.

For the common option:

Relative Path
   See :ref:`files-blend-relative_paths`.


Main Region
===========

Navigation
----------

Entering a Directory
   A single :kbd:`LMB` click on a directory enters it.
Parent Directory :kbd:`P`
   Takes you up one level of directory.


File Drop
^^^^^^^^^

You can also drag and drop a file or directory from your file manager into the Blender File Browser.
This will move it to the directory of the dropped file, and the file will be selected.


Selection
---------

Select
   Both :kbd:`LMB` and :kbd:`RMB` clicks work.
   Holding :kbd:`Shift` will extend the items selection.
(De)select All :kbd:`A`
   Toggles selecting all files.
Dragging
   Dragging with :kbd:`LMB` starts a :ref:`box selection <tool-select-box>`.


Arrow Keys
^^^^^^^^^^

It is also possible to select/deselect files by "walking" through them using the arrow keys:

- Just using an arrow key, the next file in the chosen direction will be selected and all others deselected.
- Holding down :kbd:`Shift` while doing this does not deselect anything so it extends to the selection,
  plus it allows to deselect files by navigating into a block
  of already selected ones (minimum two files in sequence).
- Holding down :kbd:`Shift-Ctrl` further selects/deselects all files in between.

If no file is selected, the arrow key navigation selects the first or last file in the directory,
depending on the arrow direction.

If you select a directory and hit :kbd:`Return`, you will go into that directory
(and highlighting 'parent' ``..`` entry will bring you up one level).


File Management
---------------

Delete Files :kbd:`Delete`, :kbd:`X`
   Delete the currently selected files or directories by moving them to the operating system's "trash".

   Note, on Linux deleting directories requires KDE or GNOME.

Rename :kbd:`F2`
   Change the name for the currently selected file or directory.


.. _file_browser-previews:

Previews
--------

.. figure:: /images/editors_file-browser_previews.png

   The File Browser in *Thumbnail* mode.

In its *Thumbnail* display mode, the File Browser supports many types of previews. These include:

- Image and video formats
- Fonts
- Blend-files
- Internal :doc:`Data-blocks </files/data_blocks>`

See :doc:`Blend-files Previews </files/blend/previews>` for how to manage Blender data previews.
