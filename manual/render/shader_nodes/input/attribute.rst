.. _bpy.types.ShaderNodeAttribute:

**************
Attribute Node
**************

.. figure:: /images/render_shader-nodes_input_attribute_node.png
   :align: right

   Attribute Node.

The *Attribute* node allows you to retrieve attributes attached to an object or mesh.


Inputs
======

This node has no inputs.


Properties
==========

Name
   Name of the attribute.
   Most attributes are more easily available through the various input nodes, except for these:

   Vertex Color Layers
      These can be retrieved this by their names.
   Density
      Gives a scalar defining the density of any smoke inside
      the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
   Color
      Gives the color of the smoke inside the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
      The color and vector outputs are the same. The Factor output is an average of the channels.
   Temperature
      Gives a scalar defining the temperature of the volume. Values in the range 0 - 1 map to 0 - 1000 kelvin.
      This may be used to render physically-based fire with the Blackbody or Principled Volume shaders.
      All three outputs are the same.
   Flame
      Gives a scalar defining the density of any fire inside
      the :doc:`Fluid Domain </physics/fluid/type/domain/index>`.
      All three outputs are the same.
   Ocean Foam
      Gives a scalar defining where foam might appear when using
      an :doc:`Ocean Modifier </modeling/modifiers/physics/ocean>`.
      This depends on the name you give this property.

   .. seealso::

      For a full list of options see `This Thread <https://blender.stackexchange.com/questions/14262#14267>`__
      on the Blender Stack Exchange.


Outputs
=======

Color
   RGB color interpolated from the attribute.
Vector
   XYZ vector interpolated from the attribute.
Factor
   Scalar value interpolated from the attribute.
