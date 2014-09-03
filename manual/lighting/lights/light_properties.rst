
..    TODO/Review: {{review}} .


Lights Common Options
*********************

.. figure:: /images/25-Manual-Lighting-Lights-Properties.jpg
   :width: 312px
   :figwidth: 312px

   Lamp Properties panels


There are five types of lamps in Blender.  They share all or some of the options listed here:

Object Data
===========

Browse Light Object Data
   Click to view all lights in the current scene.
Name
   The name of the currently selected light object data.  Edit to change the name.
Number of Users
   The number of light objects sharing the light object data.
F
   Create a fake user for this object data.


Preview
=======

A quick preview of the light settings.


Lamp

----


Distance
   The :guilabel:`Dist` field indicates the number of Blender Units (BU)
   at which the intensity of the current light source will be half of its intensity.
   Objects less than the number of BU away from the lamp will get more light,
   while objects further away will receive less light.
   Certain settings and lamp falloff types affect how the :guilabel:`Distance` field is interpreted,
   meaning that it will not always react the same;
   see the page about :doc:`light falloff </lighting/lights/light_attenuation>`.


- The :guilabel:`Sun` and :guilabel:`Hemi` Lamps are another class of Lamps which uses a constant falloff. Those lamps don't have a :guilabel:`Dist` field, and are often called "Base Lighting Lamps".

Energy
   The intensity of the light source's illumination (from ``0.0`` to ``10.0``).
Color
   The color of the light source's illumination. Opens a color swatch.
Negative
   Let the lamp cast negative light.
This Layer Only
   The Lamp only illuminates objects on the same layer the lamp is on.
Specular
   The Lamp creates specular highlights.
Diffuse
   The Lamp does diffuse shading.


