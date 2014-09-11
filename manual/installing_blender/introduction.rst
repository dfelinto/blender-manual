Installing the Binaries
***********************

Blender is available both as a binary executable and as source code on the `Blender website <http://www.blender.org/>`__.
To download Blender, select the right binary for your system from the `download page <http://www.blender.org/download/>`__ .

For the online manual hosted at the wiki, you can generally use the most recent version of
Blender located at the Blender Foundation website
(although all of the features from the newest release version may not be fully updated).  If
you are using a published version of this manual it is recommended that you use the Blender
version included on the Guide CD-ROM.  In the following text,
whenever "download" is mentioned,
those using the book should instead retrieve Blender from the CD-ROM.


Downloading and installing the binary distribution
==================================================

Binary distributions are provided for the following operating system families:


- :doc:`Windows </installing_blender/windows>`
- :doc:`Linux </installing_blender/linux/introduction>`
- :doc:`Mac OSX </installing_blender/mac>`
- :doc:`FreeBSD </installing_blender/other_oss>`

Some unofficial distributions may exist for other operating systems, but as they're not
supported by the Blender Foundation, you should report any issues you may have with them directly to their maintainers.

Binaries for the Macintosh operating systems are provided for two different hardware
architectures (x86 for Intel and AMD processors, and PowerPC),
and for the choice between statically linked or dynamically loaded libraries.

The installer will create files and several folders in two locations on your computer:
one set of folders is for the Blender program,
and the other is a set of folders for your user data.
You must have administrator authorization to create these. The folders are:

- ~/.blender - configuration information (mostly prompts in your native language)
- blendcache_.B - temporary space for physics simulation information (soft-bodies, cloth, fluids)
- scripts - python scripts that extend Blender functionality
- tmp - temporary output, intermediate renders


Hardware Support
================

Blender supports 64-bit hardware platforms, removing the 4GB addressable memory limit.

Blender also supports multi-CPU/core chips such as the Intel Core-Duo and AMD X2 chips. A
:guilabel:`Threads` setting is provided in the performance section of the render options to
indicate how many cores to use in parallel when rendering.
The :guilabel:`Auto-detect` setting will utilize all the cores available on your system, while
the :guilabel:`Fixed` setting allows the user to manually specify the number of cores to be
used when rendering.

Blender supports a wide variety of pen-based tablets on all major operating systems,
in particular OS X, Windows XP, and Linux distros.

Information on how to make render times shorter can be found in the :doc:`Render </render/performance/introduction>` section of the manual.


Developers platforms
====================

A list of platforms used by Blender developers can be found here: http://wiki.blender.org/index.php/Dev:Ref/Supported_platforms


Compiling the Source
====================

There are presently two build systems for compiling Blender on supported operating systems.
Consult the `Building Blender <http://wiki.blender.org/index.php/Dev:Doc/Building_Blender>`__
web page for more information about compiling a custom build of Blender for your machine.
