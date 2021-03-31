
***************
Discombobulator
***************

This add-on creates a greeble object based on selected faces.
It quickly creates science fiction style panels across your mesh.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Mesh then Discombobulator to enable the script.


Interface
=========

.. figure:: /images/addons_add-mesh_discombobulator_ui.jpg
   :align: right
   :width: 310px

Located in the :menuselection:`3D Viewport --> Add --> Mesh` menu.

Discombobulator works in mesh Object Mode and mesh Edit Mode.


Instructions
============

#. Select the quad faces you want to add greebles to.
#. :menuselection:`3D Viewport --> Add --> Mesh --> Discombobulator`.
#. Now you will see the interface but nothing happens to the mesh.
#. It's useful at this point to read the *Usage Information* at the top of the panel.
#. With the default settings press *OK* and you will see a new mesh object created that has raised areas.
#. Let's look at the settings below.


Protrusions Settings
--------------------

Make Protrusions
   This checkbox turns on the functions for protrusions.
   If you turn it off, nothing will happen when you run the script.
   You may want to turn Protrusions off if you are using only the Doodads function described further below.

Min/Max Height
   Adjust the height of the protrusions, you can use negative and positive values.
   The negative values will create the protrusions on the opposite side of the selected face(s).

Min/Max Taper
   Adjust the taper of the protrusions. This will affect the pointiness of the protrusions.

1, 2, 3, 4
   These checkboxes provide options for the subdivision of the faces or the amount of protrusions per face.
   Based on random, if you have all selected, each face will have either 1, 2, 3 or 4 protrusions.
   Use only one or any combination and the faces will only have your selected value(s).

Repeat Protrusions
   This button creates extra levels of protrusions built on top of the first set of protrusions.
   It's important not to set this too high as it may take time to compute.
   Note also that repeating protrusions is based on face normals and
   will create protrusions on all faces created in the previous iteration.


Doodads Settings
----------------

This checkbox allows you to use your own mesh object and have it applied on top of the protrusions.

Doodads can be a little tricky to set up:

#. Select the object(s) you want to use as a doodad.
#. Run Discombobulator and press *Pick Doodad*.
#. Select your mesh to scatter doodads on and run Discombobulator.


Materials Settings
------------------

These settings allow you to add materials to the sides and tops of the protrusions.

#. It's best to set up your materials first. Add two different materials to your mesh (two materials slots).
#. Number 0 will be the first slot in your materials, number 1 will be the second slot.
#. Run Discombobulator and you can pick the material for the top or sides.


.. admonition:: Reference
   :class: refbox

   :Category:  Add Mesh
   :Description: Add Greeble type effect to a mesh.
   :Location: :menuselection:`3D Viewport --> Add --> Mesh`
   :File: add_mesh_discombobulator folder
   :Author: Evan J. Rosky (syrux)
   :Maintainer: To Do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
