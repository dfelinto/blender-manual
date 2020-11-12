.. highlight:: sh

***********************
Installation on Windows
***********************

This guide covers the following topics:

#. `Installing Python`_ (used to "convert" the source files to HTML)
#. `Installing SVN and Downloading the Repository`_
#. `Setting up the Build Environment`_


Installing Python
=================

#. Download the `Python installation package <https://www.python.org/downloads/>`__ for Windows.
   In this guide version 3.6.x is used.
#. Install Python with the installation wizard.
   Please make sure that you enable the "Add Python to PATH" option:

   .. figure:: /images/about_contribute_install_windows_installer.png

      The option must be enabled so you can build the manual with the make script.

   All other settings can remain as set by default.


Installing SVN and Downloading the Repository
=============================================

In this guide, we will use TortoiseSVN though any Subversion client will do.

#. Download `TortoiseSVN <https://tortoisesvn.net/downloads.html>`__ for Windows.
#. Install TortoiseSVN with the installation wizard. When choosing which features will be installed,
   it is recommended that you enable *command line client tools* to give you access to SVN from the command line
   (there is no harm in doing this, and it may be helpful if you ever run into any trouble).
#. Once the installation has finished,
   create a new folder that will contain everything related to the Blender Manual.
   In this guide, we will use ``C:\blender_docs``.
#. Open the new folder, right-click and choose *SVN Checkout...* from the context menu.
#. In the *URL of repository* field, enter: ``https://svn.blender.org/svnroot/bf-manual/trunk/blender_docs``.
#. In the *Checkout directory* field, enter: ``C:\blender_docs``.
#. Click *OK* -- the repository will now be downloaded
   which may take a few minutes depending on your internet connection.


Setting up the Build Environment
================================

- Open a Command Prompt. (Run as Administrator)
- Enter the ``blender_docs`` folder which was just added by the SVN checkout::

     cd C:\blender_docs

- Inside that folder is a file called ``requirements.txt`` which contains a list of all the dependencies we need.
  Install all the dependencies using Python's ``pip`` command::

     pip install -r requirements.txt

- If all goes well, you should see the following message when it is finished::

     Successfully installed Jinja2 MarkupSafe Pygments Sphinx docutils sphinx-rtd-theme Cleaning up...

During the setup, some warnings may be shown, but do not worry about them.
However, if any errors occur, they may cause some problems.

.. note::

   Every now and then you may want to make sure your dependencies are up to date using::

      pip install -r requirements.txt --upgrade


------------------------

Continue with the next step: :doc:`Building </about/contribute/build/windows>`.
