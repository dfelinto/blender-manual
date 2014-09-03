
Opening Files
*************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`File --> Open`
   | Hotkey:   :kbd:`F1`


Description
===========

Blender uses the ``.blend`` file format to save nearly everything: objects, scenes,
textures, and even all your user interface window settings.


 .. warning::

	Blender expects that you know what you are doing! When you load a file, you
	are **not** asked to save unsaved changes to the scene you were previously
	working on, completing the file load dialog is regarded as being enough
	confirmation that you didn't do this by accident.

**Make sure that you save your files.**


.. figure:: /images/File-openwindow.jpg


Using the File Browser and Folder Navigation
============================================

To load a Blender file from disk, press :kbd:`F1`. The :guilabel:`File Browser` window,
as shown above, will open.

The upper text box displays the current directory path,
and the lower text box contains the selected filename. :kbd:`P`
(or the :guilabel:`P` button) moves you up to the parent directory.

The + and - buttons allow you to cycle through numbered files by increasing or decreasing the
number at the end of the file name.

Click on a folder to go inside of it,
or click on a file then press the :guilabel:`Open Blender File` to open it

Clicking :guilabel:`Cancel` will close the file browser window and return to the program.


Side Panel
==========

The panel on the left displays different ways to find files and several options.
To load a file, select it with :kbd:`lmb` and then press :kbd:`enter`,
or click the :guilabel:`Open File` button.
A file can also be loaded by simply clicking :kbd:`mmb` over its name.


System
------

The system menu contains a list of drives that are available to navigate through to find
files. Click on one to jump to that drive.


Bookmarks
---------

These are folders that you want to be able to access often without having to navigate to them
in the file browser. To add a directory to the bookmark menu, navigate to that folder,
then click the :guilabel:`Add` button.
To remove a folder from the list, simply click the :guilabel:`X` icon nexto to it.


Recent
------

This is a list of recently accessed folders. You can control how many folders appear in this
list by going to the :guilabel:`File` tab of the user :guilabel:`Preferences`,
in the box labeled :guilabel:`Recent Files`.


Open Options
============

Inside each .blend file, Blender saves the user interface - the screen layouts. By default,
this saved UI is loaded, overriding any user defaults or current screen layouts that you have.
If you want to work on the blend file using your current defaults, start a fresh Blender,
then open the file browser (:kbd:`F1`). Turn off the :guilabel:`Load UI` button,
and then open the file.


The Header Panel
================

The Header contains several tools for navigation files.
The four arrow icons allow you to:


- :guilabel:`Move to previous folder`
- :guilabel:`Move to next folder`
- :guilabel:`Move up to parent directory`
- :guilabel:`Refresh current folder`

Create a new folder inside the current one by clicking the :guilabel:`Create New Directory`
icon.

The other icons allow you to control what files are visible and how they are displayed.
You can:


- :guilabel:`Display files as a short list`
- :guilabel:`Display files as a detailed list`
- :guilabel:`Display files as thumbnails`

You can sort files:


- :guilabel:`Alphabetically`
- :guilabel:`By file type`
- :guilabel:`By Date of last edit`
- :guilabel:`By file size`

Filtering controls which file types are shown. Click the :guilabel:`Enable Filtering` icon,
and toggle which types are shown:


- :guilabel:`Folders`
- :guilabel:`Blend files`
- :guilabel:`Images`
- :guilabel:`Movie files`
- :guilabel:`Scripts`
- :guilabel:`Font files`
- :guilabel:`Music files`
- :guilabel:`Text files`


Other File Open Options
=======================

From the :guilabel:`File` menu, you can also open files with the following tools:

:guilabel:`Open Recent`
   Lists recently used files. Click on one to load it in.
:guilabel:`Recover Last Session`
   This will load the ``quit.blend`` file Blender automatically saves just before exiting. So this option enables you to recover your last work session, e.g. if you closed Blender by accident...
:guilabel:`Recover Auto Save`
   This will open an automatically saved file to recover it.


Security
========

Blender is aimed at production level use and relies heavily on Python,
a powerful scripting language. Python can be used in Blender to create new tools,
importers and exporters, and also to drive animation rigs.
With Python scripting there are endless possibilities in what you can create with Blender.

Part of Python's power comes from having full access to your system,
however this power can also be misused in the wrong hands. It's possible
(but not terribly likely) for dishonest people to distribute .
blend files containing scripts that may damage your system.
These scripts can be attached as part of animation rigs,
so that they will be run when such a .blend file is opened.


 .. warning::

	Always be very careful when downloading .blend files and tools from
	un-trustworthy sources!


Protection
----------

.. figure:: /images/Manual-Introduction-Security-trusted-source.jpg

To protect against malicious .blend files,
it's possible to prevent any embedded scripts from running when you open a .blend file.
This will mean that custom tools or rigs using Python features will not work,
but this won't be a problem for .blend files that don't use these
(such as material libraries),
and will at least give you a chance to better evaluate what risks might be inside.

By default, Blender will trust all files and run scripts automatically.
If you don't trust the file, and want protection, you can disable 'Trusted source' in the
File→Open dialog in the properties section on the bottom left.
Un-trusted files will disable embedded Python scripts after opening the file.


