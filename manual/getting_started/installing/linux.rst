
*******************
Installing on Linux
*******************

Check the :doc:`Downloading Blender </getting_started/installing/index>`
page to find the minimum requirements and where to get Blender (if you have not done so yet).


Install from blender.org
========================

Download the Linux version for your architecture and uncompress the file to the desired location
(e.g. ``~/software`` or ``/usr/local``).

Blender can now be launched by double-clicking the executable.

When using this method of installation, it is possible to have multiple versions of Blender installed.

For ease of access, you can configure your system by adding a menu entry or shortcut for Blender.
You may also associate blend-files with Blender so that when selected from the file browser,
they will automatically open in Blender.
These settings are typically found in conjunction with the Window Manager settings. (Gnome or KDE.)


Install from Package Manager
============================

Some Linux distributions may have a specific package for Blender in their repositories.

Installing Blender via the distribution's native mechanisms ensures consistency with other packages on the system
and may provide other features (given by the package manager),
such as listing of packages, update notifications and automatic menu configuration.
Be aware, though, that the package may be outdated compared to the latest official release,
or not include some features of Blender.
For example, some distributions do not build Blender with CUDA support, for licensing reasons.

If there is a specific package for your distribution, you may choose what is preferable and most convenient,
otherwise, the official binary is available on `blender.org <https://www.blender.org/download/>`__.


Install from Snap
=================

`Snap <https://snapcraft.io/>`__ is a universal package manager designed to work across a range of distributions.
Assuming snap is already installed, Blender can be installed through snap with::

   snap install blender

Installing from this method has a benefit that updates to Blender are automatically installed.
Blender from Snap should have a more consistent distribution then individual package managers.


Running from the Terminal
=========================

See :doc:`Launching from the terminal </advanced/command_line/launch/linux>`.


Avoiding Alt+Mouse Conflict
===========================

Many Window Managers default to :kbd:`Alt-LMB` for moving windows,
which is a shortcut that Blender uses to simulate a three button mouse.
You can either have this feature disabled :menuselection:`Preferences --> Input --> Emulate 3 Button Mouse`
or you can change the Window Manager settings to use the *Meta* key instead (also called *Super* or *Windows key*):

Gnome
   Enter the following in a command line (effective at next login):

   .. code-block:: sh

      gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier '<Super>'

KDE
   :menuselection:`System Settings --> Window Management --> Window Behavior --> Window Actions`,
   Switch from 'Alt' to 'Meta' key.


Updating on Linux
=================

On Linux there are various ways of updating Blender. This section covers the most common approaches.


Updating from blender.org
-------------------------

When an update for Blender is released, it can be downloaded directly
from the `Blender website <https://www.blender.org/download/>`__
and installed using the steps described in the section `Install from blender.org`_.


Updating with a Package Manager
-------------------------------

Many Linux distributions have packages for Blender available, which can be installed
using the distribution's package manager. After installation,
Blender can be updated using the same steps as updating any other application.


.. seealso::

   The Splash screen :doc:`/getting_started/configuration/defaults` page for information
   about import settings from previous Blender versions and on other quick settings.
