.. index:: Nodes; Attribute; Attribute Color Ramp

********************
Attribute Color Ramp
********************

Maps values from a float attribute to their corresponding color, based on a color ramp.
The resulting colors are stored on the geometry in a color attribute.

.. figure:: /images/modeling_modifiers_nodes_attribute-color-ramp.png
   :align: center

   Attribute Color Ramp Node.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   Name of the attribute that is used as input.
   It should be a float attribute with values between zero and one.

Result
   Name of the attribute where the output is stored.
   If the attribute does not exist yet, it is created.


Properties
==========

Color Ramp
   For controls see :ref:`ui-color-ramp-widget`.


Outputs
=======

Geometry
   Standard geometry output.
