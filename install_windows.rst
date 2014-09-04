
Installation guide for the Blender Manual on MS-Windows
*******************************************************

In this guide Microsoft Windows 8.1 is used.


Installing git on your computer
===============================

- Download git installation package for Windows from here: http://git-scm.com/download/win

   *In this guide version 1.9.4 is used.*

- Install git with the installation wizard.

   *In this guide the default settings are used. git will be installed to C:\\Program Files (x86)\\Git*

- To check the installation start the program Git Bash from the start menu. 

   *The Git Bash is started and a console prompt $ is shown, in the following mentioned as prompt.*

.. tip::

   You can use the Windows clipboard,
   if you click on the Git Bash program icon in the left window corner and use the commands under Edit.


Installing Python on your computer
==================================

- Download Python installation package for Windows from here: https://www.python.org/downloads/

   *In this guide version 3.4.1 is used.*

- Install Python with the installation wizard.
 
   *In this guide the default settings are used. Python will be installed to C:\\Python34*

- You can check the installation with the following steps
   - Start the Git Bash.
   - Run ``cd /c/Python34/`` at the prompt.
   - Run ``python`` at the prompt. The Python shell is started and the Python version is shown.
   - Type ``exit()`` at the Python prompt and press Enter to exit the Python shell.


Downloading the Blender Manual git repository
=============================================
- Create a new folder on your disk with your Windows Explorer.

  *In this guide C:\\blender\\ is used.*

- Start the Git Bash, if it is not running.
- Move into the new folder:

  .. code-block:: bash

     cd /c/blender

- To download the git repository of the Blender Manual to your disk, run this command at the prompt:

  .. code-block:: bash

     git clone git://git.blender.org/blender-manual.git

  *If the download is finished the prompt comes back with* ``$``
  *and on the disk a new folder blender-manual (C:\\blender\\blender-manual) is created.*


Setting up the local copy
=========================

- Open the file "C:\\blender\\blender-manual\\requirements.txt" with a text editor (e.g. notepad).
- Remove the last line ``wsgiref==0.1.2`` and save the file.

  *This line must be deleted because with Python 3.4.1 the package wsgiref is already
  installed and otherwise during the next steps it would be come to an error.*

- Start the Git Bash, if it is not running.
- Move into the new folder blender-manual of your local clone of the downloaded
  git repository with running the command at the prompt.

  .. code-block:: bash

     cd /c/blender/blender-manual

     /c/Python34/Scripts/pip install -r requirements.txt

  *A lot of information are logged. At the end the prompt comes back with* ``$`` *and above the line:*

  ``Successfully installed Jinja2 MarkupSafe Pygments Sphinx docutils sphinx-rtd-theme Cleaning up...`` ...is shown.

  During the setup some warnings are shown, they are no problem, it's important that no errors are shown.


Building the Blender manual the first time
==========================================

- Start the Git Bash, if it is not running.
- Move into the blender-manual folder and build the manual by running the commands:

  .. code-block:: bash

     cd /c/blender/blender-manual

     /c/Python34/Scripts/sphinx-build -b html ./manual ./html

  *The building process takes some time you can see a % progress running.
  At the end the line "build succeeded" is shown and the prompt comes back.
  The Blender Manual is build in the subfolder html (C:\\blender\\blender-manual\\html).*

- You can exit the Git Bash with running the command ``exit`` at the prompt.
- Open the file "C:\\blender\\blender-manual\\html\\contents.html" in your web browser and read the manual.

At this point the installation guide for the Blender Manual on Microsoft Windows is finished.
The next steps for editing the manual are shown in the Blender Manual project documentation.

