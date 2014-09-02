
..    TODO/Review: {{review}} .


Setting the default Scene
*************************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`File --> Save Startup File`
   | Hotkey:   :kbd:`ctrl-u`


When you start Blender or start a new project with the menu entry :menuselection:`File --> New` or using
the shortcut :kbd:`ctrl-N`, a new Scene is created from the default Scene stored in the
Blender install directory and it includes the default :guilabel:`User Preferences`.
This default Scene could instead be another .
blend file stored outside of Blender's default install directory.
You can save user preferences to the default Scene that comes with Blender,
or use another .blend file as a startup file with your customized user preferences.


.. figure:: /images/(Doc_26x_Manual_Vitals_Default_Scene)_(Save_Startup_File_Dialog)_(GBV266FN).jpg

   Save User Settings popup


To change the default scene, make all of the desired changes to the current scene or current
file and press :kbd:`ctrl-U`.
Note that if you are using another .blend file when you press :kbd:`ctrl-U`, this file
will be the default startup file instead of the one that comes with the default Blender
install.

The :guilabel:`Save Startup File` popup confirmation will appear.
Click :kbd:`lmb` on the :guilabel:`Save Startup File` popup or press :kbd:`Enter`.


Press :kbd:`esc` to abort.


Restoring the Default Scene to Factory Settings
***********************************************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`File --> Load factory Settings`
   | Hotkey:   Undefined, you can add one for your :doc:`Keymap » </preferences/input>`


To restore the default scene to the factory settings,
:kbd:`lmb` in :menuselection:`File --> Load Factory Settings`. This will restore all :guilabel:`User
Preferences` back to the original :guilabel:`Factory Settings`. To save the changes, use
:kbd:`ctrl-u` and your Factory Settings will be saved as the default Scene for Blender.


.. note:: User Preferences Window

   For more information about the Editor Window for User Preferences or how to clean your preferences manually, please read the chapter about :doc:`User Preferences </preferences>`


