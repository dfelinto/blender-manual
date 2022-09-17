
######################
  Installing Blender
######################

Blender is released approximately every three months.
You can keep up to date with the latest changes through
the `release notes <https://www.blender.org/download/releases/>`__.


System Requirements
===================

Blender is available for download on Windows, macOS, and Linux.
Always check that the graphics drivers are up to date and that OpenGL is well supported.
Blender has a set of `minimum and recommended requirements <https://www.blender.org/download/requirements/>`__;
so make sure these are met before trying to install Blender.

Support for other hardware such as graphic tablets and 3D mice are covered later in
:doc:`Configuring Hardware </getting_started/configuration/hardware>`.


Download Blender
================

Blender offers a variety of different binary packages to choose from depending on their level of stability.
Each package has the trade off of newest feature versus stability.
The package that is right for you depends on your requirements for those two.
A studio for example might want to have *long-term support*, while a hobbyist may want newer features,
while others may just want to test upcoming features.
Each package described below has something just right for everyone.

`Stable Release <https://www.blender.org/download/>`__
   A package that contains the latest features and is considered stable without regressions.
   A new stable version is available about every three months.

`Long-term Support <https://www.blender.org/download/lts/>`__
   A package designed for long-lasting projects requiring a very stable version of Blender.
   :abbr:`LTS (Long-Term-Support)` releases are supported for two years
   and will not have any new features, API changes or improvements.
   A new long-term support version is available every year.

`Daily Builds <https://builder.blender.org/download/>`__
   A package updated daily to include the newest changes in development.
   These versions are not as thoroughly tested as the stable release, and might break,
   although they are official and usually not highly experimental.

.. note::

   Blender's source code is available for free to either reference or
   to `Build from Source <https://wiki.blender.org/wiki/Building_Blender>`__.
   While normal users are **not** expected to compile Blender, it does have advantages:

   - Blender is always up to date.
   - It allows access to any version or branch where a feature is being developed.
   - It can be freely customized.

The procedure for installing a binary, either the latest stable release or a daily build, is the same.
Follow the steps for your platform.

.. note::

   Blender doesn't have a built-in updating system. This means you will need to update Blender yourself
   by following the upgrade steps described in the sections below.


.. toctree::
   :maxdepth: 1
   :caption: Installation Guides

   linux.rst
   macos.rst
   windows.rst
   steam.rst
