.. index:: Modeling Modifiers; Geometry Nodes Modifier
.. _bpy.types.NodesModifier:

***********************
Geometry Nodes Modifier
***********************

The *Geometry Nodes* modifier creates a modifier with a node group which defines its functionality.

.. figure:: /images/modeling_modifiers_generate_geometry-nodes_panel.png

   A new Geometry Nodes modifier with a new node group.

This modifier is supported by mesh, curve, text, and volume objects.


Options
=======

Node Group
   A :doc:`Node Group </interface/controls/nodes/groups>` with the geometry input and output.
   Those are respectively what is received and passed to the previous and next modifier in the stack.
   See :doc:`Nodes </modeling/geometry_nodes/index>` for all available nodes.

Inputs
   A list of the node group's inputs which can have unique values even
   if the group is shared among multiple modifiers.

   .. _bpy.ops.object.geometry_nodes_input_attribute_toggle:

   If the input is connected to a :doc:`Field </modeling/geometry_nodes/fields>` socket,
   there will be a toggle to switch between using a single value for the input or
   using an attribute on the input geometry. Using an attribute for input means the
   value can be different for every element.

   .. note::
      The :ref:`attribute domain <attribute-domains>` used to access the attribute is defined by the
      node the input is connected to.


Output Attributes
-----------------

By connecting a field socket to the group output node,
you can create custom :doc:`Attributes </modeling/geometry_nodes/attributes_reference>`
from a :doc:`Field </modeling/geometry_nodes/fields>` output of any node in the node tree.
The domain of the attribute must be specified in the group node's output properties.
Note, this does not work with :doc:`Instanced Data </modeling/geometry_nodes/instances>`.
