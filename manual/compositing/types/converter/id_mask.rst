.. _bpy.types.CompositorNodeIDMask:

************
ID Mask Node
************

.. figure:: /images/compositing_node-types_CompositorNodeIDMask.png
   :align: right
   :alt: ID Mask Node.

The *ID Mask Node* can be used to access an alpha mask per object or per material.


Inputs
======

ID Value
   Input for the *Object Index* or *Material Index* render pass.
   Which is an output of the :doc:`Render Layers node </compositing/types/input/render_layers>` or
   the :doc:`Image node </compositing/types/input/render_layers>` with a multi-layer format.


Properties
==========

Index
   Selection of the previously specified index.
Anti-Aliasing
   This post-processing filter smooths the mask edges. See :term:`Anti-Aliasing`.


Outputs
=======

Alpha
   The mask is white where the object is and black where it is not.
   If the object is transparent, the alpha mask represent that with gray values.


Setup
=====

An index can be specify for any object or material in the scene.
The Object Index can be set in :menuselection:`Properties --> Object Properties --> Relations --> Pass Index`
and :menuselection:`Material --> Settings --> Pass Index` for the Material Index.
To be accessible after rendering, *Object Index* or *Material Index* render pass has to be enabled.

.. figure:: /images/compositing_types_converter_id-mask_relations-panel.png

   Object Pass Index.


Example
=======

In this example, the left rear red cube is assigned Pass Index 1, and the right cube Pass Index 2.
Where the two cubes intersect, there is going to be noticeable pixelation because they come together
at a sharp angle and are different colors. Using the mask from object 1,
which is smoothed (anti-aliased) at the edges, we use a *Mix Node* set on *Multiply*
to multiply the smoothed edges of the image, thus removing those nasty lines, thus, being smoothed out.

.. figure:: /images/compositing_types_converter_id-mask_example.png

   ID Mask node example.
