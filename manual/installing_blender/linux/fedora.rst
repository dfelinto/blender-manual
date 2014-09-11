Fedora based systems
********************

Fedora is the upstream distro for Redhat Enterprise Linux, and is used by Redhat
to test new technologies which are eventually used within the official RHEL releases.
This means that Fedora is quite bleeding edge and the libraries and software that are
included with Fedora are usually quite up-to-date.


Installing Missing Blender dependencies with yum
================================================

If you have recently installed Fedora, the first thing you should do is update your system.
To do this, type the following command in a terminal window and reboot when it's finished:

``sudo yum -y update``

Note: You will be asked to enter your root password, don't worry if you don't actually see
anything on the screen when you type since your password is not echoed to the screen for security reasons.

By default, Fedora is missing the SDL library, which is required by Blender.
To install this, type the following command in the terminal window (after updating with the previous command):

``sudo yum -y install SDL``

.. tip:: It is important that you type 'SDL' and not 'sdl', case matters.

Now that you have all the dependencies installed, you can go to the
`download page <http://www.blender.org/download>`__, and choose a version to install.


Determining your hardware configuration
=======================================

Blender comes in two different architectures, a 32 bit version and 64 bit version.
If you have a 32 bit computer platform you need to download and use the 32 bit version of Blender,
otherwise you should download the 64 bit version of Blender.

You can determine whether you're running a 32 bit or 64 bit system by running the ``arch`` command
in the terminal.

If the output is 'x86_64', you have a 64 bit system and should download the 64 bit version of Blender.
If it's something else, like 'i686', you should download the 32 bit version.

.. tip:: If you are using a 64 bit system of Fedora you can also use the 32 bit version of Blender, but doing so will mean you cannot use more than 4GB of memory.


Downloading Blender
===================

Once you have determined which version of Blender you want to download,
you can click on the corresponding link on the Blender Download Website.


.. figure:: /images/(Doc_26x_Debian_Ubuntu)_(Download_Pre_Compiled_Blender_Org_Linux)_(GNV1210FN).jpg
   :width: 600px
   :figwidth: 600px

   Blender Download Webpage


Once you do click on a link your web browser will possibly display a download dialog box
asking you how you want to download Blender.


.. figure:: /images/installing_blender_linux_fedora_firefox_download.jpg
   :width: 600px
   :figwidth: 600px

   Firefox File Download Dialog Box


In the file browser dialog box make sure the option 'Save File' is selected.
Then click the OK button.
This will download the Blender software to your Downloads directory.

With your web browser window still selected press :kbd:`CTRL+SHIFT+Y`.
This will open your browser download window.
Right click on the Blender entry and select Open.


.. figure:: /images/installing_blender_linux_fedora_firefox_download_list.jpg
   :width: 600px
   :figwidth: 600px

   Firefox Download List Open


This will open the Blender software archive file in Fedora's default archive manager.

When the archive manager is displayed right click on the directory entry displayed in the
archive manager and select the Extract entry from the popup menu that is displayed.


.. figure:: /images/installing_blender_linux_fedora_extracting_blender.jpg
   :width: 600px
   :figwidth: 600px

   Archive Manager Extraction of Blender


Once the Extract entry is selected an Extract dialog box will be display,
in this dialog box you can choose the location that you want to extract the Blender files to.


.. figure:: /images/installing_blender_linux_fedora_extract_to_folder.jpg
   :width: 600px
   :figwidth: 600px

   Archive Manager Extraction Location & Options


Make sure that in the Extract dialog box that the options All Files and Re-create Folders are
both selected.  Then you can press the Extract button and the Blender archive file will be
extracted to whatever location you choose.

Once you have extracted the files from the Blender archive you will have a new directory at
the location you extracted Blender to.


Executing Blender after it has been extracted
=============================================

Once you have extracted the archive, you can start Blender by opening a terminal window and
changing directory to the directory Blender was extracted to:

``cd ~/Download/blender-2.65a-linux-glibc211-i686``

The above command would change into your home directory, from there it would change into your
Downloads directory and from there it would change into the directory Blender was extracted to
(in this case blender-2.65a-linux-glibc211-i686).  Obviously if you extracted Blender to a
different directory or are using a different version of Blender you would update the above
command as appropriate.

Once you are in the directory the Blender binary is located in type the following command at
the terminal

``./blender``

At this point if everything went well, you should see Blender displayed on screen.

.. tip:: Hardware or Software OpenGL mode

   There are 2 different ways of starting Blender.  The first way is in Hardware Accelerated OpenGL mode, in this mode if your graphics card has hardware support for OpenGL drawing commands, Blender will use it. Blender will perform much faster when it is run in Hardware Accelerated mode. By default, Blender will try to user Hardware Accelerated mode, but some graphics cards either don't work at all or don't display information in Blender correctly
   when run this way. If this happens for you then you can run Blender in Software OpenGL mode by typing:

   ``./blender-softwaregl``

   When started in this way Blender will use your CPU to process OpenGL drawing commands rather
   than using the dedicated hardware on your graphics card. This will result in Blender
   performing more slowly when doing 3D graphical tasks but it will also enable Blender to
   display correctly when it would not otherwise.


Operating System keyboard conflicts
===================================

Blender has a massive amount of hotkeys that it uses. However, some of the hotkeys that Blender uses
are also used by Gnome Shell. What follows is a list of the major conflicting keyboard shortcuts and how to change them.


.. tip::
   Unfortunately the Gnome Shell developers have a habit of changing the way you alter the keyboard shortcut assignment. If you find that methods mentioned no longer work, please do a google search and you will find how to do it. The following commands work for Fedora 19/20 when using Gnome Shell.


ALT+Left Mouse Button
---------------------

:kbd:`ALT+LMB` is a common keyboard shortcut used by Blender. It is also used by Gnome Shell to move windows around. Because of this conflict, using this keyboard shortcut to do edge loop selection does work as expected. A common fix for this is to tell Gnome Shell to instead use :kbd:`SUPER+LMB`. The :kbd:`SUPER` key is also often called the :kbd:`Windows` key.

To have Gnome Shell use the :kbd:`SUPER` key rather than :kbd:`ALT`
key when moving windows on the desktop, type the following command in a terminal window:

``dconf write "/org/gnome/desktop/wm/preferences/mouse-button-modifier" "'<Super>'"``


Obtaining snapshot builds of Blender
====================================

If you want to get snapshot bulds of Blender from the git repository, you have a couple of options.

Graphicall is a Blender users site where many different snapshots of Blender are compiled by users
and made available for download. This website hosts many builds of Blender with experimental features enabled,
such as the different branches from GSOC's.

- `www.graphicall.org <http://www.graphicall.org>`__

The BuildBot is the official Blender Foundation snapshot builds from git.
The builds provided here are built daily for all supported platforms.

- `builder.blender.org <http://builder.blender.org/download>`__

If you want to build Blender from source, you can follow the official instruction on the wiki.
Building Blender from source is not difficult compared to trying to build other software of comparable complexity,
but it takes some preparation and configuration to get right.

- `Offical guide <http://wiki.blender.org/index.php/Dev:Doc/Building_Blender>`__

If you still need help then you can always go to the #blendercoders channel on the Freenode IRC
network and report the problem you are having. Many of coders are busy or in other timezones, so you may
have to wait a while for them to see your message. If you don't have an irc client on your machine
you can access the #blendercoders channel in your browser through the link below.

- `#blendercoders on Freenode <https://kiwiirc.com/client/irc.freenode.net/blendercoders>`__

Being a Fedora user there's one more option for obtaining the latest development snapshot
version of Blender from git. It comes in the form of a special script which automatically
downloads all the source code and library dependencies that are required to build Blender
directly from source code on a Fedora system. This will only work for recent versions of Fedora,
and has only been tested to work with 32 bit and 64 bit PC/Intel versions of Fedora
(the script probably won't work for Mac computers). This is *extremely* experimental and not officially
supported by the Blender Foundation. But if you are a person who really wants to build Blender yourself
and can't make sense of the official instructions, this script makes it slightly easier (when it works).

- `AutoCompileBlender Script <http://wiki.blender.org/index.php?title=User:Terrywallwork&section=1>`__


Enabling RPM Fusion for Fedora
==============================

Fedora aims to be an entirely open source operating system, and as such it does not include any closed
source software in its official repositories. This means that some important software such as codecs,
libraries, and proprietary drivers are not available in a Fedora system.

To get around some of these limitations an external software repository was set up called RPM Fusion,
which provides lots of extra software that does not meet the licensing standards of the Fedora Project.

Some features of Blender require certain libraries (i.e. FFMPEG codecs) that are only provided in
RPM Fusion, so you may want to install RPM Fusion for your system.

You can find instructions for how to do this on the `RPM Fusion website <http://rpmfusion.org/Configuration>`__


Installing CUDA for GPU rendering with Cycles
=============================================

*ToDo*
