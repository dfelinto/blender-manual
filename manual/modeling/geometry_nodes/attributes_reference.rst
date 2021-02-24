.. index:: Geometry Nodes; Attribute Reference

**********
Attributes
**********

An *attribute* is a generic term to describe data stored per-element in a geometry data-block.
For example, every vertex can have an associated number or vector.
Attributes can be adjusted by the nodes in the *Attribute* category, but some other nodes can
change the values of specific attributes.

.. note::

   The blue attribute sockets are just string sockets, used to find which attribute in the geometry to use.

.. note::

   Attribute data types are converted implicitly where possible, just like node sockets.


Built-In Attributes
===================

Built-in attributes always exist, and cannot be removed. Their data type can not be changed.

.. list-table::
   :widths: 10 10 50
   :header-rows: 1

   * - Name
     - Type
     - Notes

   * - **position**
     - *Vector*
     - Built-in attribute describing vertex or point locations, in the modifier
       object's transform space. Any node that changes the location of points will adjust
       this attribute, like the :doc:`Transform </modeling/geometry_nodes/geometry/transform>`
       and :doc:`Point Translate </modeling/geometry_nodes/point/point_translate>` nodes.

   * - **radius**
     - *Float*
     - A built-in atribute on point cloud data created by the
       :doc:`Point Distribute Node </modeling/geometry_nodes/point/point_distribute>`
       Used to set the size for the points in the viewport.

   * - **material_index**
     - *Integer*
     - Used to specify the material slot for every polygon in a mesh.


Naming Conventions
==================

These attributes do not exist by default, but are used implicitly by certain nodes. The data type of these
attributes can be changed, just like any attribute besides the built-in attributes.

If the attributes don't exist yet, a default value is used, which can depend on the situation.
For example, in the :doc:`Point Instance Node </modeling/geometry_nodes/point/point_instance>`,
the default value for `scale` is a unit scale of (1, 1, 1), but the default value for new attributes
in the "Attribute" nodes is zero.

.. list-table::
   :widths: 10 10 50
   :header-rows: 1

   * - Name
     - Type
     - Notes

   * - **rotation**
     - *Vector*
     - Used in the :doc:`Point Instance Node </modeling/geometry_nodes/point/point_instance>` to
       control the rotation of instanced objects or collections. Adjusted by
       the :doc:`Point Rotate Node </modeling/geometry_nodes/point/point_rotate>` and the
       :doc:`Align Rotation to Vector Node </modeling/geometry_nodes/point/align_rotation_to_vector>`.

   * - **scale**
     - *Vector*
     - Used in the :doc:`Point Distribute Node </modeling/geometry_nodes/point/point_distribute>` 
       to control the scale of instances. Adjusted by the 
       :doc:`Point Scale Node </modeling/geometry_nodes/point/point_rotate>` or other attribute nodes.

   * - **id**
     - *Integer*
     - Created by the :doc:`Point Distribute Node </modeling/geometry_nodes/point/point_distribute>` to
       provide stability when the shape of the input mesh changes. The values are large,
       with no order. The attribute values are used by nodes that generate randomness, like
       the :doc:`Attribute Randomize Node </modeling/geometry_nodes/attribute/attribute_randomize>`.


Custom Attributes
=================

Vertex groups, UV maps and vertex colors are available as attributes in geometry nodes.
They are referred to by their name.
Naming collisions (e.g. a vertex group and a uv map with the same name) should be avoided.
If there is a naming collision, only one of the attributes is accessible in geometry nodes.

Attributes with any other name can also be created by nodes, when the name is used for the first time.

Note that geometry nodes does not always produce e.g. vertex groups if a node like
:doc:`Join Geometry </modeling/geometry_nodes/geometry/join_geometry>` is used.
Similarly, if the data type of a vertex group attribute is changed from the initial "Float" type,
the attribute will no longer be a vertex group.
