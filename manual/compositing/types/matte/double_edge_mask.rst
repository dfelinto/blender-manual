.. _bpy.types.CompositorNodeDoubleEdgeMask:

*********************
Double Edge Mask Node
*********************

.. figure:: /images/compositing_node-types_CompositorNodeDoubleEdgeMask.png
   :align: right

   Double Edge Mask Node.

The *Double Edge Mask* node creates a gradient between two masks.


Inputs
======

Inner Mask
   A mask representing the inside shape, which will be fully white.
Outer Mask
   A mask representing the outside shape, which will fade from black at its edges
   to white at the *Inner Mask*.


Properties
==========

Inner Edge
   All
      All shapes in the *Inner Mask* contribute to the gradient, even ones that do
      not touch the *Outer Mask* shape.
   Adjacent Only
      Only shapes in the *Inner Mask* that overlap with the *Outer Mask* contribute
      to the gradient.

   .. list-table::

      * - .. figure:: /images/compositing_types_matte_double-edge-mask_all.png

             All.

        - .. figure:: /images/compositing_types_matte_double-edge-mask_adjacent.png

             Adjacent Only.

Buffer Edge
   Keep In
      Parts of the *Outer Mask* that touch the edge of the image are treated as if
      they stop at the edge.
   Bleed Out
      Parts of the *Outer Mask* that touch the edge of the image are extended
      beyond the boundary of the image.

   .. list-table::

      * - .. figure:: /images/compositing_types_matte_double-edge-mask_in.png

             Keep In.

        - .. figure:: /images/compositing_types_matte_double-edge-mask_bleed.png

             Bleed Out.


Outputs
=======

Mask
   Standard mask output.


Example
=======

.. youtube:: VcjEfoNIHZs
