
**************
Modifier Tools
**************

A small collection of utilities for managing modifiers.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Interface then Modifier Tools to enable the script.


Description
===========

Apply All
   Applies all modifiers on all selected objects in 3D Viewport.
   This option is also available in the *Apply* menu.
Delete All
   Removes all modifiers on all selected objects in 3D Viewport.
Viewport Visibility
   Toggles viewport visibility on/off of modifiers for all selected objects in the 3D Viewport.
   Some modifiers will be skipped as they don't have their visibility exposed in the interface
   (for example the Collision modifier). In that case, a message will be added with the modifier's name.
Toggle Stack
   Expands/collapses the stack of modifiers on the active object.
   While in collapsed state, only the header of a panel is shown.


Usage
=====

When enabled and the object has modifiers the additional helpers appear above the modifier stack.


Known Limitations
=================

- To access the options, the active object has to have modifiers.
- Sometimes applying modifiers can fail for some objects.
  For instance, if the modifier is disabled (i.e. Boolean Modifier that doesn't have the Object field defined --
  Mesh used for Boolean operation or objects that share linked data).


.. admonition:: Reference
   :class: refbox

   :Category:  Interface
   :Description: Modifiers specials show/hide/apply selected.
   :Location: :menuselection:`Properties --> Modifiers`
   :File: space_view3d_modifier_tools folder
   :Author: meta-androcto, saidenka
   :Maintainer: meta-androcto
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
