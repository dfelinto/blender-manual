
Material Preview
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Preview


The Preview panel gives a quick visualization of the active material and its properties,
including its :guilabel:`Shaders`, :guilabel:`Ramps`,
:guilabel:`Mirror Transp` properties and :guilabel:`Textures`.
It provides several shapes that are very useful for designing new shaders: for some shaders
(like those based on :guilabel:`Ramp` colors, or a Diffuse shader like :guilabel:`Minnaert`),
one needs fairly complex or specific previewing shapes to decide if the shader being designed
achieves its goal.


Options
-------

Flat XY plane
   Useful for previewing textures and materials of flat objects, like walls, paper and such.
Sphere
   Useful for previewing textures and materials of sphere-like objects, but also to design metals and other reflective/transparent materials, thanks to the checkered background.
Cube
   Useful for previewing textures and materials of cube-like objects, but also to design procedural textures. Features a checkered background.
Monkey
   Useful for previewing textures and materials of organic or complex non-primitive shapes. Features a checkered background.
Hair strands
   Useful for previewing textures and materials of strand-like objects, like grass, fur, feathers and hair. Features a checkered background.
Large Sphere with Sky
   Useful for previewing textures and materials of sphere-like objects, but also to design metals and other reflective materials, thanks to the gradient Sky background.

Preview uses OSA (oversampling). Whatever the preview option, it will make use of OSA
(oversampling) in order to provide better quality.
Disable this option if your computer is already slow or old.


Examples
--------

+------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-Flat.jpg  |.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-Sphere.jpg |.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-Cube.jpg     +
+   :width: 200px                                                  |   :width: 200px                                                   |   :width: 200px                                                     +
+   :figwidth: 200px                                               |   :figwidth: 200px                                                |   :figwidth: 200px                                                  +
+                                                                  |                                                                   |                                                                     +
+   Plane preview.                                                 |   Sphere preview.                                                 |   Cube preview.                                                     +
+------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-Monkey.jpg|.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-Strands.jpg|.. figure:: /images/Manual-2.5-Material-MatMenu-Preview-SphereSky.jpg+
+   :width: 200px                                                  |   :width: 200px                                                   |   :width: 200px                                                     +
+   :figwidth: 200px                                               |   :figwidth: 200px                                                |   :figwidth: 200px                                                  +
+                                                                  |                                                                   |                                                                     +
+   Monkey preview.                                                |   Hair Strands preview.                                           |   Sky Sphere preview.                                               +
+------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+


