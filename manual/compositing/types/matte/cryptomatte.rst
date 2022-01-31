
****************
Cryptomatte Node
****************

.. figure:: /images/compositing_node-types_CompositorNodeCryptomatte.png
   :align: right

   Cryptomatte Node.

The Cryptomatte node uses the Cryptomatte standard to efficiently create mattes for compositing.
Cycles and Eevee output the required render passes, which can then be used in the Compositor
or another compositor with Cryptomatte support to create masks for specified objects.

Unlike the Material and Object Index passes, the objects to isolate are selected in compositing,
and mattes will be anti-aliased and take into account effects like motion blur and transparency.


Inputs
======

Image
   Standard color input.


Properties
==========

Source
   The source of the Cryptomatte data.

   :Render:
      Use Cryptomatte data that are stored as part of the render.
   :Image:
      Use Cryptomatte data that are stored inside a multilayered OpenEXR image.

Scene
   Scene selector.
   Only available when Render Source is selected.

Image
   Image selector.
   Only available when Image Source is selected.

Cryptomatte Layer
   Selector of the Cryptomatte layer.

Matte ID
   List of object and material crypto IDs to include in matte.
   This can be used for example to quickly clear all mattes by deleting the text
   or used to copy-and-paste crypto IDs from other software.


Outputs
=======

Image
   A colored output of the input image with the matte applied to only include selected layers.
Matte
   A black-and-white alpha mask of all the selected crypto layers.
Pick
   A colored representation of the Cryptomatte pass which can be used as a higher contrast
   image for color picking.


Usage
=====

#. Enable Cryptomatte Object render pass in the Passes panel, and render.
#. In the compositing nodes, create a Cryptomatte node and select the Cryptomatte layer.
#. Attach a Viewer node to the combined pass of the render layers.
#. Use the Cryptomatte Add/Remove button to sample objects from the Compositor backdrop.
#. Use the Matte output of the Cryptomatte node to get the alpha mask.

The Image editor, UV editor, node backdrop or Movie Clip editor can be used to pick a Cryptomatte sample.
They don't need to show any Cryptomatte layer. The node will use the sample image coordinate to
sample in the Cryptomatte layer that is selected in the node.


Example
=======

In the example below, you can see the pass output on the right side.
On the left side you can see a couple of objects that were selected through the *Cryptomatte* node.
Notice how the cube on the left has a sphere-shaped cut-out from a sphere that was not selected in the node.

.. figure:: /images/compositing_types_matte_cryptomatte_example.png


Limitations
===========

- Cryptomatte sidecars (metadata files) are not supported.
- Cryptomatte node cannot be used in node groups.
