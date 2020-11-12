
*********
MeasureIt
*********

MeasureIt is an add-on designed for displaying measures in the viewport,
making the process of design objects with exact measures, easier.
These tools are extremely useful for any job that requires exact measurements,
including architectural projects, technical design and 3D printing.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then MeasureIt to enable the script.


Interface
=========

.. figure:: /images/addons_3d-view_measureit_example.jpg
   :align: center
   :width: 640px


Overview
--------

Located in the :menuselection:`3D Viewport --> Sidebar --> View tab`.
The MeasureIt Tools panel is described below.

To view the measures you need to press the *Show* button.
Many measure styles appear grayed out in the menu, these are active in Edit Mode.

- The Mesh Debug sub panel has extra display options.
- The Items sub panel appears after adding a measure. This contains the color settings for each measure.
- The Configuration sub panel contains the font settings.
- The Render sub panel contains the render settings.


Usage
=====

- Mesh vertex to vertex measure: Length between vertices in the same mesh.
- Mesh vertex labeling: Add a label to any mesh vertex.
  This allows identify easily different areas or objects in the scene.
- Object to object: Distance between object origins, vertex to origin or vertex to vertex.
- Object to origin: Distance between object origin to scene origin or vertex to scene origin.
- Allows work with different scales.
- The measures can be used with meshes, empties, lights, and cameras.

As all measure definitions are saved in the blend-file, you can save the file and
the next time you use it, the measures will be ready.


.. admonition:: Reference
   :class: refbox

   :Category:  3D View
   :Description: Tools for measuring objects in the 3D Viewport.
   :Location: :menuselection:`3D Viewport --> Sidebar --> View tab`
   :File: measureit folder
   :Author: Antonio Vazquez (antonioya)
   :Maintainer: Antonio Vazquez (antonioya)
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
