.. _bpy.types.CompositorNodeAntiAliasing:

*************
Anti-Aliasing
*************

.. figure:: /images/compositing_node-types_CompositorAntiAliasing.png
   :align: right

   Anti-Aliasing Node.

The Anti-Aliasing node removes distortion artifacts around edges known as aliasing.


Inputs
======

Image
   Standard image input.


Properties
==========

Threshold
   Controls edge detection sensitivity across the whole image.

Contrast Limit
   Controls contrast level to consider when detecting edges.

   The human eye does not perceive all edges equally. For instance,
   it tends to mask low contrast edges in the presence of much higher contrasts in the surrounding area.
   Therefore, applying anti-aliasing to unperceived edges will produce artifacts.
   This parameter quantifies the difference between low contrast and high contrast neighboring edges.

Corner Rounding
   Detect corners to help preserve the original shape.
   Setting *Corner Rounding* to 0 means no corner detection and no corner rounding will take place.
   The higher the value the better corners will be preserved, i.e. resemble original image.


Outputs
=======

Image
   Standard image output.


Examples
========

.. list-table:: The Anti-Aliasing node has three properties shown here.

   * - .. figure:: /images/compositing_types_filter_antialiasing-node_example-1-threshold.gif
          :align: center

          Changing threshold affects all edges.

     - .. figure:: /images/compositing_types_filter_antialiasing-node_example-2-contrast_limit.gif
          :align: center

          Changing contrast limit affects neighboring edges below contrast limit.

.. list-table:: The effect of corner rounding.

   * - .. figure:: /images/compositing_types_filter_antialiasing-node_example-3-corner_rounding-off.png

         Corner detection and rounding off (set to 0).
         Notice how anti-aliasing node smooths the corner because it treats it as an artifact.

     - .. figure:: /images/compositing_types_filter_antialiasing-node_example-3-corner_rounding-on.png

         Corner detection and rounding on.
         Setting this value to 1 tells the anti-aliasing node the sharp edges
         around the corner are not an artifact and should therefore be reserved.
