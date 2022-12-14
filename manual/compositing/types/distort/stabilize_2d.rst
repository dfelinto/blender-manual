.. index:: Compositor Nodes; Stabilize 2D
.. _bpy.types.CompositorNodeStabilize:

*****************
Stabilize 2D Node
*****************

.. figure:: /images/compositing_node-types_CompositorNodeStabilize.webp
   :align: right
   :alt: Stabilize 2D Node.

Stabilizes the footage according to the settings set in
:menuselection:`Movie Clip Editor --> Properties --> Stabilization --> 2D Stabilization`.
For more information,
see :doc:`2D Stabilization </movie_clip/tracking/clip/sidebar/stabilization/index>`.


Inputs
======

Image
   Standard color input.


Properties
==========

Movie Clip
   The movie clip whose stabilization to use.

Interpolation
   Various methods for the stabilization.
   Usually, the same as used in
   :menuselection:`Movie Clip Editor --> Properties --> Stabilization --> 2D Stabilization --> Interpolate`.
   For technical details on their difference,
   `see this <https://www.mathworks.com/help/vision/ug/interpolation-methods.html>`__.
   But for most purposes, default of Bilinear should suffice.

Invert
   Invert the stabilization. If the stabilization calculated is to move the movie clip up by 5 units,
   this will move the movie clip down by 5 units.


Outputs
=======

Image
   Standard color input.
