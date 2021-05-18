.. index:: Geometry Nodes; Attribute Sample Texture
.. _bpy.types.GeometryNodeAttributeSampleTexture:

************************
Attribute Sample Texture
************************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-sample-texture_node.png
   :align: center

   Attribute Sample Texture node.

The *Attribute Sample Texture* node evaluates a texture for every point and
stores the resulting colors in a new attribute.
The mapping attribute can be anything that can be converted to a 3D vector.
Typically, either the name of a UV map or the ``position`` attribute is used.

.. note::

   UV maps can only be accessed after a Point Distribute node currently.
   This is a limitation that will be resolved.

An *Attribute Sample Texture* node can be added quickly by dragging a texture data-block into the node editor.


Inputs
======

Geometry
   Standard geometry input.

Texture
   The texture the node should sample colors from.

Mapping
   Name of the attribute that determines where the texture is evaluated.

Result
   Name of the attribute where the results are stored.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.
