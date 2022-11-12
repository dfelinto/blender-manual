
*************************
Blender ID Authentication
*************************

This add-on allows you to authenticate your Blender with your `Blender ID <https://id.blender.org/>`__ account.
This authentication can then be used by other add-ons, such as the
`Blender Cloud add-on <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/System/BlenderCloud/>`__.


Installation
============

- Sign up for an account at the `Blender ID site <https://id.blender.org/>`__ if you don't have an account yet.
- Open Blender and go to Preferences then the Add-ons tab.
- Click System then Blender ID authentication to enable the script.
- Log in with your Blender ID and password. You only have to do this once.

Your password is never saved on your machine, just an access token.
It is stored next to your Blender configuration files, in:

- Linux:

  .. parsed-literal:: $HOME/.config/blender/|BLENDER_VERSION|/config/blender_id

- macOS:

  .. parsed-literal:: $HOME/Library/Application Support/Blender/|BLENDER_VERSION|/config/blender_id

- Windows:

  .. parsed-literal:: %APPDATA%\\Blender Foundation\\Blender\\\ |BLENDER_VERSION|\\config\\blender_id


Description
===========

- To Do

.. reference::

   :Category: System
   :Description: Stores your Blender ID credentials for usage with other add-ons.
   :Location: :menuselection:`Preferences --> Add-on tab`
   :File: blender_id folder
   :Author: Sybren A. Stüvel, Francesco Siddi, and Inês Almeida
   :License: GPLv2+
   :Note: This add-on is bundled with Blender.
