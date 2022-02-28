
*********
Real Snow
*********

This add-on allows you to add snow on top of objects.

The main principle behind this addon is to add a particle system of metaballs
on top of the selected object and transform it to mesh.

.. figure:: /images/addons_object_real-snow_example.png
   :align: center
   :width: 700px


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Real Snow to enable the script.


Usage
=====

#. Open the `Real Snow` tab available in the N sidebar of the 3D Viewport.
#. Select objects you want to add snow on top.
#. Change the parameters and click on the "Add Snow" button to generate the snow.

.. note::

  - The snow material use microdisplacement to achieve realistic result.
    You need to change the `render engine` to Cycles and `Feature Set`
    to experimental in order for microdisplacement to be working.
  - You can also add snow only on part of an object by selecting the faces
    in edit mode and activating the "Selected Faces" toggle in the panel.


Parameters
==========

.. figure:: /images/addons_object_real-snow_ui.png
   :align: right
   :width: 220px

Coverage
   Percentage of the area to be covered by snow.
Height
   Height of the snow to apply (define the radius of the metaballs).
Selected Faces
   If enabled, only the selected faces will receive snow otherwise every face pointing up will be covered by snow.
Add Snow
   Adds the snow on the selected objects.

.. reference::

   :Category:  Object
   :Description: Generate snow mesh.
   :Location: :menuselection:`3D Viewport --> Properties Panel`
   :File: real_snow.py
   :Author: Marco Pavanello (Wolf), Leon Zandman (Izandman), Drew Perttula
   :License: GPL
   :Note: This add-on is bundled with Blender.
