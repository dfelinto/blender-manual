
Introduction
============

In some situations we want to increase the render speed,
access blender remotely to render something or build scripts that use blender command line.

One advantage of using command line is that we don't need the X server (in case of Linux)
and as a consequence we can render remotely by SSH or telnet.

*Note!*
Arguments are executed in the order they are given!
blender -b file.blend -a -x 1 -o //render
...Wont work, since the output and extension is set after blender is told to render.

Always position **-f** or **-a** as the last arguments.


Syntax
======

blender [-b <dir><file> ''[-o <dir><file>''][-F <format>]
[-x ''[0|1]''][-t <threads>][-S <name>][-f <frame>]
[-s <frame> -e <frame> -a]] [[-P <scriptname> [-- <parameter>]]


Render Options:
---------------

-b or --background <file>
Load <file> in background (often used for UI-less rendering)

-a or --render-anim
Render frames from start to end (inclusive)

-S or --scene <name>
Set the active scene <name> for rendering

-f or --render-frame <frame>
Render frame <frame> and save it.
+<frame> start frame relative, -<frame> end frame relative.

-s or --frame-start <frame>
Set start to frame <frame> (use before the -a argument)

-e or --frame-end <frame>
Set end to frame <frame> (use before the -a argument)

-j or --frame-jump <frames>
Set number of frames to step forward after each rendered frame

-o or --render-output <path>
Set the render path and file name.
Use // at the start of the path to
render relative to the blend file.
The # characters are replaced by the frame number, and used to define zero padding.
ani_##_test.png becomes ani_01_test.png
test-######.png becomes test-000001.png
When the filename does not contain #, The suffix #### is added to the filename
The frame number will be added at the end of the filename.
eg: blender -b foobar.blend -o //render_ -F PNG -x 1 -a
//render_ becomes //render_####, writing frames as //render_0001.png//

-E or --engine <engine>
Specify the render engine
use -E help to list available engines

-t or --threads <threads>
Use amount of <threads> for rendering and other operations
[1-64], 0 for systems processor count.


Format Options:
---------------

-F or --render-format <format>
Set the render format, Valid options are...
TGA IRIS JPEG MOVIE IRIZ RAWTGA
AVIRAW AVIJPEG PNG BMP FRAMESERVER
(formats that can be compiled into blender, not available on all systems)
HDR TIFF EXR MULTILAYER MPEG AVICODEC QUICKTIME CINEON DPX DDS

-x or --use-extension <bool>
Set option to add the file extension to the end of the file


Animation Playback Options:
---------------------------

-a <options> <file(s)>
Playback <file(s)>, only operates this way when not running in background.
-p <sx> <sy>    Open with lower left corner at <sx>, <sy>
-m      Read from disk (Don't buffer)
-f <fps> <fps-base>     Specify FPS to start with
-j <frame>  Set frame step to <frame>
-s <frame>  Play from <frame>
-e <frame>  Play until <frame>


Window Options:
---------------

-w or --window-border
Force opening with borders (default)

-W or --window-borderless
Force opening without borders

-p or --window-geometry <sx> <sy> <w> <h>
Open with lower left corner at <sx>, <sy> and width and height as <w>, <h>

-con or --start-console
Start with the console window open (ignored if -b is set), (Windows only)

--no-native-pixels
Do not use native pixel size, for high resolution displays (MacBook 'Retina')


Game Engine Specific Options:
-----------------------------

-g Game Engine specific options
-g fixedtime        Run on 50 hertz without dropping frames
-g vertexarrays     Use Vertex Arrays for rendering (usually faster)
-g nomipmap     No Texture Mipmapping
-g linearmipmap     Linear Texture Mipmapping instead of Nearest (default)


Python Options:
---------------

-y or --enable-autoexec
Enable automatic python script execution

-Y or --disable-autoexec
Disable automatic python script execution (pydrivers & startup scripts),
(compiled as non-standard default)


-P or --python <filename>
Run the given Python script file

--python-text <name>
Run the given Python script text block

--python-console
Run blender with an interactive console

--addons
Comma separated list of addons (no spaces)


Debug Options:
--------------

-d or --debug
Turn debugging on


- Prints every operator call and their arguments
- Disables mouse grab (to interact with a debugger in some cases)
- Keeps python sys.stdin rather than setting it to None

--debug-value <value>
Set debug value of <value> on startup


--debug-events
Enable debug messages for the event system

--debug-handlers
Enable debug messages for event handling

--debug-jobs
Enable time profiling for background jobs.

--debug-python
Enable debug messages for python

--debug-wm
Enable debug messages for the window manager

--debug-all
Enable all debug messages (excludes libmv)


--debug-fpe
Enable floating point exceptions

--disable-crash-handler
Disable the crash handler


Misc Options:
-------------

--factory-startup
Skip reading the "startup.blend" in the users home directory


--env-system-datafiles
Set the BLENDER_SYSTEM_DATAFILES environment variable

--env-system-scripts
Set the BLENDER_SYSTEM_SCRIPTS environment variable

--env-system-python
Set the BLENDER_SYSTEM_PYTHON environment variable


-nojoystick
Disable joystick support

-noglsl
Disable GLSL shading

-noaudio
Force sound system to None

-setaudio
Force sound system to a specific device
NULL SDL OPENAL JACK


-h or --help
Print this help text and exit

-v or --version
Print Blender version and exit

--
Ends option processing, following arguments passed unchanged. Access via python's sys.argv


Other Options:
--------------

/?
Print this help text and exit (windows only)

--verbose <verbose>
Set logging verbosity level.

-R
Register .blend extension, then exit (Windows only)

-r
Silently register .blend extension, then exit (Windows only)


Examples
========

Render a picture
----------------

- blender -b file.blend -o //file -F JPEG -x 1 -f 1


- '''-b'''

       Load blender without an interface

- '''file.blend'''

       File .blend to render

- '''-o //file'''

       Directory + Target image file

- '''-F JPEG'''

       JPEG image format

- '''-x 1'''

       Ensures an extension .jpg to the file name

- '''-f 1'''

       Render frame 1


Render a movie
--------------

- blender -b file.blend -x 1 -o //file -F MOVIE -s 003 -e 005 -a


- '''-b'''

       Load blender without an interface

- '''file.blend'''

      File .blend to render

- '''-x'''

      Ensures an extension .avi to the movie

- '''-o //file'''

       Directory + Target image file

- '''-F MOVIE'''

       This saves a .AVI movie with low compression

- '''-s 003 -e 005 -a'''

       Set start frame to 003 and end frame to 005. '''''Important:''''' ''You can use -s or -e, but if they're not in order, they'll not work!''


Launch Blender with a specified engine
--------------------------------------

The flags that are used are -E engine or --engine engine


- blender --engine CYCLES

You can list the available engines by using


- blender --engine help

or

- blender -E help

Example output

found bundled python: /home/satishg/bin/blender-2.65a-linux-glibc27-x86_64/2.65/python
Blender Engine Listing:
BLENDER_RENDER
BLENDER_GAME
CYCLES

[1]    Done                          ~/bin/blender-2.65a-linux-glibc27-x86_64/blender --engine help


Platforms
=========

How to actually execute Blender from the command line depends on the platform and where you
have installed Blender. Here are basic instructions for the different platforms.


Windows
_______

Open the Command Prompt, go to the directory where Blender is installed,
and then run the blender command.


- cd c:\<blender installation directory>
- blender


Mac OS X
________

Open the Terminal application, go to the directory where Blender is installed,
and run the executable within the app bundle, with commands like this:


- cd /Applications/Blender
- ./blender.app/Contents/MacOS/blender

If you need to do this often,
you can make an alias so that typing just 'blender' in the terminal works.
For that you can run a command like this in the terminal (with the appropriate path).


- echo "alias blender=/Applications/Blender/blender.app/Contents/MacOS/blender" >> ~/.profile

If you then open a new terminal, the following command will work:


- blender


Linux
_____

Open a terminal, then go to the directory where Blender is installed,
and run the blender command like this.


- cd <blender installation directory>
- ./blender

If you have Blender installed in your PATH
(usually when Blender is installed through a linux distribution package),
you may be able to simple do this:


- blender

{{Page/Footer|Doc:2.5/Manual/Render/Bake|Doc:2.5/Manual/Post-production}}

[[Category:Rendering]]
[[Category:Command line]]