.. index:: Geometry Nodes; Attribute Reference

**********
Attributes
**********

An *attribute* is a generic term to describe data stored per-element in a geometry data-block.
For example, every vertex can have an associated number or vector.
Attributes can be altered by connecting a value to the *Group Output* node,
but also many nodes can change the values of specific attributes.

.. note::

   Attribute data types and domains are converted implicitly where possible, just like node sockets.


Named Attributes
================

In the modifier, it is possible to access attributes with names, created and used in other areas
of Blender like shaders, painting, and UV mapping. The attribute can be chosen with a name, 
and the string input allows you to search and choose existing attributes.

.. figure:: /images/modeling_geometry-nodes_attribute-reference_search.png
   :align: center

   Attribute Search.

The attribute search gives a bit of context about each attribute.
To the left of the menu, the attribute domain is shown followed by the attribute name.
To the right of the menu, the attribute data type is shown.


Anonymous Attributes
====================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_attribute-field.png
   :align: center

   The *Normal* and *Rotation* ouputs are examples of attribute fields,
   which refer to an attribute stored on a geometry.

Attributes exposed in Blender's interface all have names. However, for convenience, attributes
can be passed around with node sockets in geometry nodes groups. In these cases, an *Attribute Field*
output is created, which can be used by nodes to find attribute data in an input geometry.


Attribute Domains
=================

All attributes have an associated domain and type. Knowing the domain of an attribute is important
because it defines how it may be interpolated and used in nodes and shading.
You can use the :doc:`Spreadsheet Editor </editors/spreadsheet>` to determine the domains of attributes.

- **Point** domain attributes are associated with single locations in space with a position.
   * Vertices of a mesh
   * Points of a point cloud
   * Curve control points
- **Edge** domain attributes are associated with the edges of a mesh.
- **Face** domain attributes are associated with the faces of a mesh.
- **Face Corner** domain attributes are associated with the corners of the faces of the mesh.
  An example is a UV map attribute.
- **Spline** domain attributes are associated with a group of connected curve control points.

.. note::

   For point cloud objects, every attribute has the *point* domain.


Attribute Data Types
====================

The type of an attribute is the kind of data stored at each element.

   :Float: Floating-point value
   :Integer: 32-bit integer
   :Boolean: True or false value
   :Vector: 3D vector with floating-point values
   :Color: RGBA color with floating-point precision

.. _geometry-nodes_builtin-attributes:


Built-In Attributes
===================

Built-in attributes always exist, and cannot be removed. Their data type and domain cannot be changed.

.. list-table::
   :widths: 10 10 10 50
   :header-rows: 1

   * - Name
     - Type
     - Domain
     - Notes

   * - ``position``
     - *Vector*
     - *Point*
     - Built-in attribute describing vertex or point locations, in a geometry's local space.
       Any node that changes the location of points will adjust this attribute, 
       like the :doc:`Transform </modeling/geometry_nodes/geometry/transform>`
       and :doc:`Set Position </modeling/geometry_nodes/geometry/set_position>` nodes.

   * - ``radius``
     - *Float*
     - *Point*
     - A built-in attribute on point clouds used to set the size for the points in the viewport.
       Also built-in on curves, where it controls the size of each curve control point when
       converted to a mesh, or for other operations.

   * - ``id``
     - *Integer*
     - *Point*
     - Created by the :doc:`/modeling/geometry_nodes/point/distribute_points_on_faces` to
       provide stability when the shape of the input mesh changes, and used on instances to create
       motion blur. The values expected to be large, with no order. The attribute values are used 
       by nodes that generate randomness, like the :doc:`/modeling/geometry_nodes/utilities/random_value`.
       Unlike other built-in attributes, this attribute is not required, and can be removed if necessary.

   * - ``material_index``
     - *Integer*
     - *Face*
     - Used to specify the material slot for every face in a mesh.

   * - ``crease``
     - *Float*
     - *Edge*
     - Edge attribute used by the Subdivision Surface node and modifier.
       The values are limited to a range of 0 and 1.

   * - ``shade_smooth``
     - *Boolean*
     - *Face*
     - Attribute determining if a face should have smooth shading enabled.

   * - ``resolution``
     - *Integer*
     - *Spline*
     - Determines the number of evaluated points between two control points of a spline.

   * - ``cyclic``
     - *Boolean*
     - *Spline*
     - Determines whether the spline is cyclic or not.

   * - ``handle_left``
     - *Vector*
     - *Point*
     - Describes the location of the left handle of a curve control point, on the side
       of the curve's start. Only exists when the curve contains a Bézier spline.

   * - ``handle_right``
     - *Vector*
     - *Point*
     - Describes the location of the right handle of a curve control point, on the side
       of the curve's end. Only exists when the curve contains a Bézier spline.


Naming Conventions
==================

These attributes do not exist by default, but are used implicitly by certain parts of Blender.
The data type of these attributes can be changed, just like any attribute besides the built-in 
attributes. However, the attributes might be expected by Blender to have a certain type.

.. list-table::
   :widths: 10 10 50
   :header-rows: 1

   * - Name
     - Type
     - Notes

   * - ``velocity``
     - *Vector*
     - Used to create motion blur when rendering animations.


Custom Attributes
=================

Vertex groups, UV maps and vertex colors are available as attributes in geometry nodes.
They are referred to by their name.
Naming collisions (e.g. a vertex group and a UV map with the same name) should be avoided.
If there is a naming collision, only one of the attributes is accessible in geometry nodes.

Attributes with any other name can also be created by nodes, when the name is used for the first time.

Note that geometry nodes does not always produce e.g. vertex groups if a node like
:doc:`Join Geometry </modeling/geometry_nodes/geometry/join_geometry>` is used.
Similarly, if the data type of a vertex group attribute is changed from the initial "Float" type,
the attribute will no longer be a vertex group.
