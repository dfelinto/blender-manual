
*************
Change Layers
*************

.. _bpy.ops.armature.armature_layers:

Change Armature Layers
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Change Armature Layers`

Each armature has 32 :ref:`Layers <bpy.types.Armature.layers>` to
organize armatures by "regrouping" them into sets of bones.
Only bones in active layers will be visible/editable, but they will always be effective
(i.e. move objects or deform geometry), whether in an active layer or not.
This tool changes which layers are visible in the 3D Viewport.
To show several layers at once, :kbd:`Shift-LMB` on the desired layers to view.
To move bones to a given layer, use :ref:`bpy.ops.armature.bone_layers`.


.. _bpy.ops.armature.bone_layers:

Change Bone Layers
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Change Bone Layers`
   :Shortcut:  :kbd:`M`

Todo.
