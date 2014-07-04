
Scripting & Security
====================

The ability to include Python scripts within blend files is valuable for advanced tasks such
as rigging, automation and using the game-engine,
however it poses a security risk since Python doesn't restrict what a script can do.

Therefore, you should only run scripts from sources you know and trust.

Automatic execution is disabled by default,
however some blend files need this to function properly.

When a blend file tries to execute a script and is not allowed, a message will appear in the
header with the option to **Reload Trusted** or **Ignore** the message.


.. figure:: /images/Python_Script_AutoExec_Header.jpg
   :width: 800px
   :figwidth: 800px


Scripts in Blend Files
----------------------

Auto Execution
~~~~~~~~~~~~~~

Here are the different ways blend files may automatically run scripts.


- Registered Text-Blocks

*A text block can have its* **Register** *option enabled which means it will load on start.*

- Animation Drivers

*Python expressions can be used to* **drive** *values and are often used in more advanced rigs and animations.*

- Game Engine Auto-Start

*scripts are often used for game logic, blend files can have auto-start enabled with runs the game on load.*


Manual Execution
~~~~~~~~~~~~~~~~

There are other ways scripts in a ``blend`` file may execute that require user
interaction (therefor will run even when auto-execution is off),
but you should be aware
that this is the case since it's not necessarily obvious.


- Running a script in the text editor *(ok, this is obvious!)*.
- Rendering with FreeStyle - *FreeStyle uses scripts to control line styles*
- Running the Game-Engine.


Controlling Script Execution
----------------------------

Blender provides a number of ways to control whether scripts from a blend file are allowed to
automatically execute.

First of all, the file-selector has the option **Trusted Source** which you can use on a
case-by-case basis to control auto-execution.

However you may forget to set this,
or open a file without going through the file selector - so you can change the default
(described next).


Setting Defaults
~~~~~~~~~~~~~~~~

In the **File** section of the user-preferences there is the toggle **Auto-Run Python
Scripts**.

This means the **Trusted Source** option in the file-selector will be enabled by default,
and scripts can run when blend files are loaded without using the file selector.

Once enabled you have the option to exclude certain directories,
a typical configuration would be to trust all paths except for the download directory.


.. figure:: /images/Python_Script_AutoExec_Configure.jpg
   :width: 600px
   :figwidth: 600px


Command Line
~~~~~~~~~~~~

You may want to perform batch rendering or some other task from the command line - running
Blender without an interface.

In this case the user-preferences are still used but you may want to override them.

- Enable with ``-y`` or ``--enable-autoexec``
- Disable with ``-Y`` or ``--disable-autoexec``

Example - rendering an animation in background mode, allowing drivers and other scripts to run:
::


   blender --background --enable-autoexec my_movie.blend --render-anim


Note: these command line arguments can be used to start a regular blender instance and will
still override the user-preferences.