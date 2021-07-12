
*********
Bool Tool
*********

Todo.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Bool Tool to enable the script.


Description
===========

.. rubric:: Concepts

- Brush: Is an object used as a mask for the Boolean operation.
- Canvas: Is the object that keep the Boolean operation.

You can select any count of objects and apply all these objects to the active one as a Boolean brush.
Just select the objects that you want to be a brush,
select an object to set it as active and click in one of those operations:

Auto Boolean
   Difference :kbd:`Shift-Ctrl-NumpadMinus`
      Remove the objects to the active.
   Union :kbd:`Shift-Ctrl-NumpadPlus`
      Add the selected objects to the active object.
   Intersection :kbd:`Shift-Ctrl-NumpadAsterisk`
      Apply an intersect operation between the selected objects and the active.
   Slice :kbd:`Shift-Ctrl-NumpadSlash`
      Todo.

.. todo check if operators still there.

   Remove
      The *Remove* operation clean up some brush and restore it as a normal object.
      If you apply a Remove to a canvas, it will delete all Brushes and restore the canvas a normal object.

   Brush Viewer
      In the *Brush Viewer* you can select, exclude or remove a brush that is applied to this canvas
      (the object that keeps the result of the Boolean operation).

   All Brushes to Mesh
      Allows you to apply all the brushes to the object and convert it to a final mesh.
      (Be aware that it's a destructive process, you will lost all the interactive stuff,
      but with that you will free the process and will get it as a simple mesh.)

Brush Boolean
   Difference :kbd:`Ctrl-NumpadMinus`
      Apply direct Difference to an object.
   Union :kbd:`Ctrl-NumpadPlus`
      Apply direct Union to an object.
   Intersection :kbd:`Ctrl-NumpadAsterisk`
      Apply direct Intersection to an object.
   Slice :kbd:`Ctrl-NumpadSlash`
      Todo.


Preferences
-----------

Fast Transformation
   When enable this option in the add-on preferences your :kbd:`G`/:kbd:`R`/:kbd:`S` hotkeys will be replaced for
   a custom one that can handle objects visibility and Boolean modifiers before and
   after the transform operation to give a fast transform when using Boolean operations.
   It only works good when handling high-poly brush, if you try to use it in a low-poly brush
   when another high-poly brush is applied it will be slow yet
   since we have a bad Dependency Graph handling of that situation.

.. reference::

   :Category:  Object
   :Description: Boolean modifier tools.
   :Location: :menuselection:`3D Viewport --> Sidebar --> Edit tab`, :kbd:`Shift-Ctrl-B`
   :File: object_boolean_tools.py
   :Author: Vitor Balbio, Mikhail Rachinskiy, TynkaTopi, Meta-Androcto, Simon Appelt
   :License: GPL
   :Note: This add-on is bundled with Blender.
