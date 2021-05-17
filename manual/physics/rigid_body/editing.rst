
*******
Editing
*******

.. _bpy.ops.rigidbody.mass_calculate:

Calculate Mass
==============

.. admonition:: Reference
   :class: refbox

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Rigid Body --> Caculate Mass`

Automatically calculate mass values for rigid body objects based on their volume and desity.
The volume is calculated automatically, the desity needs to be given based on the object you are trying to simulate.

Material Preset
   A list of preset density values for real-world materials,
   if a material is not given you can research the desity and use the *Custom* preset to input the desity manually.

Desity
   When the *Custom* *Material Preset* is selected, this is the input desity to use;
   note that this value should be in kg/m\ :sup:`3` units.
