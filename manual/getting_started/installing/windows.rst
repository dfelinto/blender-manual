
*********************
Installing on Windows
*********************

Check the :doc:`Downloading Blender </getting_started/installing/index>`
page to find the minimum requirements and the different versions that are available 
for Blender (if you have not done so yet).

Download the zip-file or Windows Installer File.


Install from Windows Installer File
===================================

The Windows installer will let you choose an installation folder,
and will create an entry in the start menu as well as associate blend-files with Blender.
It requires administrator rights.


Install from Zip
================

When choosing the zip-file, you have to manually extract Blender to the desired folder,
where you can double-click the executable to run Blender.

No start menu item will be created and no blend-file association will be registered,
but there is also no need for administrator rights. You can register the file association
manually by clicking *Make Default* on the System tab of the
:doc:`Preferences </editors/preferences/system>`. Alternatively, you can run ``blender -r``
from the :doc:`Command Line </advanced/command_line/arguments>`.

.. tip:: How to Make a Portable Installation

   To keep all configuration files and installed add-ons in the executable folder,
   create a folder named ``config`` in the :ref:`LOCAL directory <blender-directory-layout>`
   of the unzipped folder.


Install from Microsoft Store
============================

Blender can be installed from the Microsoft Store by searching for Blender in the Microsoft Store
and installing it.

Blender can now be launched from the Windows Start menu.


Updating on Windows
===================

On Windows there are various ways of updating Blender. This section covers the most common approaches.


Updating from Windows Installer File
------------------------------------

When an update for Blender is released, it can be downloaded directly
from the `Blender website <https://www.blender.org/download/>`__.
The Windows installer can then be run to install the updated version of Blender.
To remove a previously installed version of Blender,
use Windows settings or control panel to uninstall the desired version.


Updating from Zip
-----------------

When an update for Blender is released, it can be downloaded directly
from the `Blender website <https://www.blender.org/download/>`__
and extracted to the desired folder, where you can double-click the executable to run Blender.
For more information on creating a portable version of Blender, see the section `Install from Zip`_.

Note, you do not have to overwrite your existing Blender installation.
It's perfectly possible to have multiple versions installed side by side.


Updating from the Microsoft Store
---------------------------------

When an update for Blender is available on the Microsoft Store, it will be downloaded
and installed automatically.

.. seealso::

   The Splash screen :doc:`/getting_started/configuration/defaults` page for information
   about importing settings from previous Blender versions and other quick settings.
