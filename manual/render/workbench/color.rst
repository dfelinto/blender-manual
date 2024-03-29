.. _bpy.types.View3DShading.color_type:

*****
Color
*****

The colors that the Workbench uses to render objects can be changed.

.. reference::

   :Panel:     :menuselection:`Render --> Color`

:Material:
   Use the color that can be set per material
   in the Viewport Display :ref:`properties-material-viewport-display` panel.
:Object:
   Use the color that can be set per object
   in the Viewport Display :ref:`properties-object-viewport-display` panel.
:Attribute:
   Display the active :ref:`Color Attribute <modeling-meshes-properties-object_data-color-attributes>`
   of an object. When an object has no active Color Attribute it will be rendered in the color set
   in the Viewport Display :ref:`properties-object-viewport-display` panel.
:Single:
   Render the whole scene using a single color. The color can be chosen.
:Random:
   A random color will be selected for every object in the scene.
:Texture:
   Display the active texture using the active UV mapping coordinates.
   When an object has no active texture the object will be rendered with the settings
   in the Viewport Display :ref:`properties-material-viewport-display` panel.
