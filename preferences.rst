
This chapter explains how to change Blender's default configuration with the :guilabel:`User
Preferences` editor.

The Blender :guilabel:`User Preferences` editor contains many of the settings that you can
change to control the way Blender behaves each time you open the application.


Open User Preferences
=====================

To open a Blender :guilabel:`User Preferences` editor go to :menuselection:`File --> User Preferences` or press :kbd:`ctrl-alt-u`\ . Mac users can press :kbd:`cmd-,`\ . You can also load the Preferences editor in any window by selecting

.. figure:: /images/User-preferences-icon.jpg


 :guilabel:`User Preferences` from the Window type selection menu.


.. figure:: /images/User-preferences.jpg
   :width: 650px
   :figwidth: 650px


This editor permits you to configure how Blender will work.
The available options are grouped into seven tabs, accessible at the top of the window.
The options are: *Interface*\ , *Editing*\ , *Input*\ , *Add-Ons*\ , *Themes*\ ,
*File* and *System*\ .


Configure
---------

Now that you have opened the :guilabel:`User Preferences` editor,
you can configure Blender to your liking.
Select what you want to change in the following list:


FIXME(Template Unsupported: Doc:RO/2.5/Manual/Interface/Configuration/index;
{{Doc:RO/2.5/Manual/Interface/Configuration/index}}
)


Save the new preferences
------------------------

Once you have set your preferences, you will need to manually save them,
otherwise the new configuration will be lost after a restart.
Blender saves its preferences to :guilabel:`userpref.blend` in your user folder.

In the :guilabel:`User Preferences` window, click on :guilabel:`Save User Settings`\ .
This will save all of the new preferences.


Load Factory Settings
---------------------

There are two ways to restore the default Blender settings:


- Go to :menuselection:`File --> Load Factory Settings` and then save the preferences with :kbd:`ctrl-u` or via the :guilabel:`User Preferences` editor.
- Delete the ``startup.blend`` file from the following location on your computer:
  - Linux: */home/*\ ``$user``\ */.blender/<code>'Version Number'/config/startup.blend* (you'll need to show hidden files).
  - Windows 7 and Windows Vista: *C:\Users\$user\AppData\Roaming\Blender Foundation\Blender\'Version Number'\config\startup.blend'
  - MacOS:* /Users/$user/Library/Application Support/Blender/'Version Number'/config/startup.blend'' (you'll need to show hidden files).

While you're in the Blender config folder,
it can be valuable to copy your Blender settings file to another folder.
In the event that you lose your configuration,
you can restore your Blender settings file with your backup copy.

