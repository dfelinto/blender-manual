.. _bpy.types.CompositorNodeCryptomatte:

*************************
Cryptomatte Node (Legacy)
*************************

.. figure:: /images/compositing_node-types_CompositorNodeCryptomatte.webp
   :align: right
   :alt: Cryptomatte Node.

The Cryptomatte node uses the Cryptomatte standard to efficiently create mattes for compositing.
Cycles and Eevee output the required render passes, which can then be used in the Compositor
or another compositor with Cryptomatte support to create masks for specified objects.

Unlike the Material and Object Index passes, the objects to isolate are selected in compositing,
and mattes will be anti-aliased and take into account effects like motion blur and transparency.

.. important::

   The Cryptomatte Legacy node is deprecated and replaced by
   :doc:`Cryptomatte Node </compositing/types/matte/cryptomatte>`.
   The legacy node will be removed in a future Blender release.


Inputs
======

Image
   Standard color input.
Crypto Passes
   Each crypto layer will be given its own render pass;
   each of these render passes must be connected to one of these crypto layer inputs.
   By default there are only four layers, see `Adding/Removing Layers`_ to add more.


Properties
==========

Add/Remove
   Adds/Removes an object or material from matte, by picking a color from the *Pick* output.
Matte ID
   List of object and material crypto IDs to include in matte.
   This can be used for example to quickly clear all mattes by deleting the text
   or used to copy-and-paste crypto IDs from other software.


Outputs
=======

Image
   A colored output of the input image with the matte applied to only include selected layers.
Matte
   A black-and-white alpha mask of the all the selected crypto layers.
Pick
   A colored representation of the Cryptomatte pass which can be used
   with a Viewer node to select which crypto passes are used to create the matte image.


Usage
=====

#. Enable Cryptomatte Object render pass in the Passes panel, and render.
#. In the compositing nodes, create a Cryptomatte node and
   link the Render Layer matching Image and Cryptomatte passes to it.
#. Attach a Viewer node to the Pick output of the Cryptomatte node.
#. Use the Cryptomatte Add/Remove button to sample objects in the Pick Viewer node.
#. Use the Matte output of the Cryptomatte node to get the alpha mask.


Adding/Removing Layers
----------------------

By default there are only four crypto layers available as inputs to the Cryptomatte node.
You can add or remove layer inputs through
:menuselection:`Sidebar --> Item --> Properties --> Add/Remove Crypto Layer`.
These operators will add/remove layers from the bottom of the pass inputs.


Example
=======

In the example below, you can see the pass output on the right side.
On the left side you can see a couple of objects that were selected through the *Cryptomatte* node.
Notice how the cube on the left has a sphere-shaped cut-out from a sphere that was not selected in the node.

.. figure:: /images/compositing_types_matte_cryptomatte_example.png
