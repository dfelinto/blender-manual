.. _bpy.types.ShaderNodeAttribute:

**************
Attribute Node
**************

.. figure:: /images/node-types_ShaderNodeAttribute.webp
   :align: right
   :alt: Attribute Node.

   Attribute Node.

The *Attribute* node allows you to retrieve attributes attached to an object or mesh.


Inputs
======

This node has no inputs.


Properties
==========

Name
   Name of the attribute.

Type
   Specifies the type of the attribute.

   :Geometry:
      The attribute is associated with the geometry of the object, and its value varies from
      vertex to vertex, or within the volume of the object.

      Most geometry attributes are directly accessible through the various input nodes, except for these:

      Vertex Color Layers
         These can be retrieved this by their names.
      Ocean Foam
         Gives a scalar defining where foam might appear when using
         an :doc:`Ocean Modifier </modeling/modifiers/physics/ocean>`.
         This depends on the name you give this property.

      .. seealso::

         For a full list of options see `This Thread <https://blender.stackexchange.com/questions/14262#14267>`__
         on the Blender Stack Exchange.
   :Object:
      The attribute name specifies a :ref:`custom property <files-data_blocks-custom-properties>` name,
      or an RNA path to a built-in property (like the single property :ref:`driver variables <drivers-variables>`).

      The values of attributes of this type are defined once per object. The name or path is looked up
      first in the object data-block, followed by the mesh data-block if not found.
      Custom properties have priority over built-in ones.

      The property value must be an integer, float, or a vector of 1 to 4 floats; properties of other types
      are ignored. If a suitable property is not found, all sockets of the node, including *Alpha*, output 0.

      .. tip::

         The ``color`` attribute will output the value of the Color field in
         the :ref:`Viewport Display <properties-object-viewport-display>` panel of
         the object, unless overridden by a custom property.
   :Instancer:
      Similar to *Object*, but the attribute is looked up in the instancer particle system settings,
      followed by the instancer object. If the current object is not instanced, or the property is
      not found, it falls back to the *Object* mode.


Outputs
=======

Color
   RGB color interpolated from the attribute.
Vector
   XYZ vector interpolated from the attribute.
Factor
   Scalar value interpolated from the attribute.
Alpha
   Alpha channel of the attribute, when available. If the attribute has no alpha channel, generally defaults to 1.

.. note::

   Currently, attributes are not supported in shaders used for the :doc:`World </render/lights/world>` or
   :doc:`Light Objects </render/lights/light_object>`.
