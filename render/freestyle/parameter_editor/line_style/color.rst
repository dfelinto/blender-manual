
Color
=====

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Color.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Color UI


In this tab you control the color of your strokes.

:guilabel:`Base Color`
   The base color for this line style.


Modifiers
---------

There are four color modifiers available, which can be mixed with the base color using the usual methods (see for example the :doc:`Mix compositing node <composite_nodes/types/color#mix_node>` for further discussion of this topic). As with other modifier stacks in Blender, they are applied from top to bottom.

:guilabel:`Influence`
   How much the result of this modifier affects the current color.


Along Stroke
~~~~~~~~~~~~

.. figure:: /images/Manual-2.6-Render-Freestyle-Color_Along_Stroke.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Color's Along Stroke modifier


The :guilabel:`Along Stroke` modifier alters the base color with a new one from a given color
ramp mapped along each stroke's length. In other words,
it applies a color ramp along each stroke.

The only settings here are those of the standard Blender color ramp!


Distance from Camera
~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Manual-2.6-Render-Freestyle-Color_Distance_From_Camera.jpg
   :width: 300px
   :figwidth: 300px

   Line Style  Color's Distance From Camera modifier


The :guilabel:`Distance from Camera` color modifier alters the base color with a new one from
a given color ramp, using the distance to the active camera as the parameter.

:guilabel:`Range Min` and :guilabel:`Range Max`
   The limits of the mapping from "distance to camera" to "color in ramp". If the current point of the stroke is at :guilabel:`Range Min` or less from the active camera, it will take the start color of the ramp, and conversely, if it is at :guilabel:`Range Max` or more from the camera, it will take the end color of the ramp. These values are in the current scene's units, not in pixels!

:guilabel:`Fill Range by Selection`
   Set the min/max range values from the distances between the current selected objects and the camera.

The other settings are those of the standard Blender color ramp!


Distance from Object
~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Manual-2.6-Render-Freestyle-Color_Distance_From_Object.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Color's Distance From Object modifiers


The :guilabel:`Distance from Object` color modifier alters the base color with a new one from
a given color ramp, using the distance to a given object as the parameter.

:guilabel:`Target`
   The object to measure distance from.

:guilabel:`Range Min` and :guilabel:`Range Max`
   The limits of the mapping from "distance to object" to "color in ramp". If the current point of the stroke is at :guilabel:`Range Min` or less from the target, it will take the start color of the ramp, and conversely, if it is at :guilabel:`Range Max` or more from the target, it will take the end color of the ramp. These values are in the current scene's units, not in pixels!

:guilabel:`Fill Range by Selection`
   Set the min/max range values from the distances between the current selected objects and the target.

The other settings are those of the standard Blender color ramp!


Material
~~~~~~~~

.. figure:: /images/Manual-2.6-Render-Freestyle-Color_Material.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Color's Material modifiers


The :guilabel:`Material` color modifier alters the base color with a new one taken from the
current material under the stroke.

You can use various properties of the materials, among which many are mono-component (i.e.
give B&W results). In this case,
an optional color ramp can be used to map these grayscale values to colored ones.

If used with the :guilabel:`Split by Material` option in the :guilabel:`Stroke` tab,
the result will not be blurred between materials along the strokes.


.. figure:: /images/Lilies_Color_Material.jpg
   :width: 400px
   :figwidth: 400px

   Material modifiers demo by T.K. `File:Lilies_Color_Material.zip <http://wiki.blender.org/index.php/File:Lilies_Color_Material.zip>`__


