.. highlight:: sh

*********************
Installation on Linux
*********************

This guide covers the following topics:

#. `Installing Dependencies`_
#. `Downloading the Repository`_
#. `Setting up the Build Environment`_


Installing Dependencies
=======================

Below are listed the installation commands for popular Linux distributions.

For the appropriate system, run the command in a terminal:

Debian/Ubuntu
   .. code-block:: sh

      sudo apt-get install python3 python3-pip subversion

Redhat/Fedora
   .. code-block:: sh

      sudo yum install python python-pip
Arch Linux
   .. code-block:: sh

      sudo pacman -S python python-pip subversion


Downloading the Repository
==========================

Simply check out the Blender Manual's repository using::

      cd ~
      svn checkout https://svn.blender.org/svnroot/bf-manual/trunk/blender_docs

The repository will now be downloaded which may take a few minutes depending on your internet connection.


Setting up the Build Environment
================================

- Open a Terminal window.
- Enter the ``blender_docs`` folder which was just added by the SVN checkout::

     cd ~/blender_docs

- Inside that folder is a file called ``requirements.txt`` which contains a list of all the dependencies we need.
  To install these dependencies, we can use the ``pip3`` command::

     sudo pip3 install -r requirements.txt

.. note::

   Every now and then you may want to make sure your dependencies are up to date using::

      sudo pip3 install -r requirements.txt --upgrade


------------------------

Continue with the next step: :doc:`Building </about/contribute/build/linux>`.
