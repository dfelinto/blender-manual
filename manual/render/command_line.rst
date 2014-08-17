
Introduction
************

In some situations we want to increase the render speed,
access blender remotely to render something or build scripts that use blender command line.

One advantage of using command line is that we don't need the X server (in case of Linux)
and as a consequence we can render remotely by SSH or telnet.

*Note!*
Arguments are executed in the order they are given!
blender -b file.blend -a -x 1 -o //render
...Wont work, since the output and extension is set after blender is told to render.

Always position ``-f`` or ``-a`` as the last arguments.

.. RST / WIKI NOTE - WE HAD THE FULL OUTPUT OF `blender --help` here,
   not sure theres much point int duplicating all info! - ideasman42


Platforms
*********

How to actually execute Blender from the command line depends on the platform and where you
have installed Blender. Here are basic instructions for the different platforms.


Windows
^^^^^^^

Open the Command Prompt, go to the directory where Blender is installed,
and then run the blender command.

.. code-block:: bat

   cd c:\<blender installation directory>
   blender


Mac OS X
^^^^^^^^

Open the Terminal application, go to the directory where Blender is installed,
and run the executable within the app bundle, with commands like this:

.. code-block:: sh

   cd /Applications/Blender
   ./blender.app/Contents/MacOS/blender

If you need to do this often,
you can make an alias so that typing just 'blender' in the terminal works.
For that you can run a command like this in the terminal (with the appropriate path).

.. code-block:: sh

   echo "alias blender=/Applications/Blender/blender.app/Contents/MacOS/blender" >> ~/.profile

If you then open a new terminal, the following command will work:

.. code-block:: sh

   blender


Linux
^^^^^

Open a terminal, then go to the directory where Blender is installed,
and run the blender command like this.

.. code-block:: sh

   cd <blender installation directory>
   ./blender

If you have Blender installed in your ``PATH``
(usually when Blender is installed through a linux distribution package),
you may be able to simple do this:

.. code-block:: sh

   blender

