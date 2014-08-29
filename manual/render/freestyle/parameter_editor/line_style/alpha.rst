
Alpha
*****

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Alpha.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Alpha UI


In this tab you control the alpha (transparency) of your strokes.

:guilabel:`Base Transparency`
   The base alpha for this line style.


Modifiers
=========

There are four alpha modifiers available, which can be mixed with the base alpha using a subset of the usual methods
(see for example the :doc:`Mix compositing node </composite_nodes/types/color#mix_node>` for further discussion of
this topic). As with other modifier stacks in Blender, they are applied from top to bottom.

:guilabel:`Influence`
   How much the result of this modifier affects the current transparency.


Along Stroke
------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Alpha_Along_Stroke.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Alpha's Along Stroke modifier


The :guilabel:`Along Stroke` modifier alters the base alpha with a new one from either a
linear progression or a custom curve, mapped along each stroke's length. In other words,
it applies the selected progression along each stroke.

:guilabel:`Mapping`
   Either a linear progression (from **0.0** to **1.0**, which may be inverted with the :guilabel:`Invert` option),
   or a custom mapping curve.


Distance from Camera
--------------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Alpha_Distance_From_Camera.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Alpha's Distance From Camera modifier


The :guilabel:`Distance from Camera` modifier alters the base alpha with a new one from either
a linear progression or a custom curve, using the distance to the active camera as parameter.

:guilabel:`Mapping`
   Either a linear progression (from **0.0** to **1.0**, which may be inverted with the :guilabel:`Invert` option),
   or a custom mapping curve.

:guilabel:`Range Min` and :guilabel:`Range Max`
   The limits of the mapping from "distance to camera" to "alpha in mapping".
   If the current point of the stroke is at :guilabel:`Range Min` or less from the active camera,
   it will take the start alpha of the mapping, and conversely,
   if it is at :guilabel:`Range Max` or more from the camera, it will take the end alpha of the mapping.
   These values are in the current scene's units, not in pixels!

:guilabel:`Fill Range by Selection`
   Set the min/max range values from the distances between the current selected objects and the camera.


Distance from Object
--------------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Alpha_Distance_From_Object.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Alpha's Distance From Object modifier


The :guilabel:`Distance from Object` modifier alters the base alpha with a new one from either
a linear progression or a custom curve, using the distance to a given object as parameter.

:guilabel:`Target`
   The object to measure distance from.

:guilabel:`Mapping`
   Either a linear progression (from **0.0** to **1.0**, which may be inverted with the :guilabel:`Invert` option),
   or a custom mapping curve.

:guilabel:`Range Min` and :guilabel:`Range Max`
   The limits of the mapping from "distance to object" to "alpha in mapping".
   If the current point of the stroke is at :guilabel:`Range Min` or less from the target,
   it will take the start alpha of the mapping, and conversely,
   if it is at :guilabel:`Range Max` or more from the target, it will take the end alpha of the mapping.
   These values are in the current scene's units, not in pixels!

:guilabel:`Fill Range by Selection`
   Set the min/max range values from the distances between the current selected objects and the target.


Material
--------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Alpha_Material.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Alpha's Material modifier


The :guilabel:`Material` modifier alters the base alpha with a new one taken from the current
material under the stroke.

You can use various properties of the materials, among which some are multi-components (i.e.
give RGB results). In that case, the mean value will be used.

:guilabel:`Mapping`
   Either a linear progression (from **0.0** to **1.0**, which may be inverted with the :guilabel:`Invert` option),
   or a custom mapping curve. Note the linear non-inverted option is equivalent to "do nothing",
   as original values from materials are already in the [0.0, 1.0] range...

If used with the :guilabel:`Split by Material` option in the :guilabel:`Stroke` tab,
the result will not be blurred between materials along the strokes.
