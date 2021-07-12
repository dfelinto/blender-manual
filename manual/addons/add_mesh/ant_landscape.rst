
*************
ANT Landscape
*************

This add-on creates landscapes and planets using various noise types. A.N.T. stands for Another Noise Tool.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Mesh then A.N.T. Landscape to enable the script.


Interface
=========

.. figure:: /images/addons_add-mesh_ant-landscape_ui.jpg
   :align: right
   :width: 220px

Located in the :menuselection:`3D Viewport --> Add --> Mesh` menu.

Located in the :menuselection:`3D Viewport --> Sidebar --> Create` tab.


Instructions
============

After creating your landscape mesh there are three main areas in
the :ref:`bpy.ops.screen.redo_last` panel to design your mesh.

- Main Settings: Object and mesh related settings like size and subdivisions.
- Noise Settings: Noise related settings that give shape to your terrain.
- Displace Settings: Settings for terrain height and edge falloff.


Landscape Panel
---------------

Landscape
   Landscape will create the mesh and add several panels and tools to the Sidebar.


Landscape Tools
---------------

Mesh Displace
   Displace selected mesh vertices along normal or X, Y, Z direction.
Weight from Slope
   Generates a weighted vertex group slope map based on the Z normal value.
Landscape Eroder
   Apply various kinds of erosion to an A.N.T. Landscape grid,
   also available in the *Weights* menu in Weight Paint Mode.


Landscape Main
--------------

Here we can adjust the main settings and regenerate the mesh.

Smooth the mesh, Triangulate the mesh, Rename and add materials that you have in your blend-file.


Landscape Noise
---------------

Here we can adjust the noise settings and refresh only those settings.

There are many settings and noise types that allow you to customize your landscape.


Landscape Displace
------------------

Here we can adjust the displacement settings and refresh only those settings.

Adjust Height, Falloff and Strata in this section.


Usage
=====

To Do


.. reference::

   :Category:  Add Mesh
   :Description: Another Noise Tool: Landscape, erosion and displace.
   :Location: :menuselection:`Sidebar --> Create tab`
   :File: ant_landscape folder
   :Author: Jimmy Hazevoet
   :Maintainer: To Do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
