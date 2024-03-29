.. index:: Geometry Nodes; Attribute Reference

.. _bpy.ops.object.attribute_add:
.. _bpy.ops.object.attribute_remove:
.. _bpy.ops.geometry.attribute_add:
.. _bpy.ops.geometry.attribute_remove:

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

Named attributes are created and used in other areas of Blender like shaders, painting, and UV mapping.
In the :doc:`modifier panel </modeling/modifiers/generate/geometry_nodes>`, a named attribute can
be used for input by clicking the icon to the left of the value button. The string input input
allows you to search and choose existing attributes from the modifier's input geometry.

.. figure:: /images/modeling_geometry-nodes_attribute-reference_search.png
   :align: center

   Attribute Search.

The attribute search gives a bit of context about each attribute.
To the left of the menu, the attribute domain is shown followed by the attribute name.
To the right of the menu, the attribute data type is shown.


.. _anonymous-attributes:

Anonymous Attributes
====================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_attribute-field.png
   :align: center

   The *Normal* and *Rotation* outputs are examples of attribute fields,
   which refer to an attribute stored on a geometry.

An anonymous attribute is a set of generic data stored on a geometry that doesn't have a name.
Usually, attributes exposed in Blender's interface all have names. However,
in geometry nodes, attributes can be passed around with node sockets.
In these cases, an *Attribute Field* output is created, which is used by
nodes to find attribute data in an input geometry.

Anonymous attributes are still stored on the geometry like other attributes, and they are even
automatically interpolated when the geometry changes with other nodes, except for a few cases.
So generally, if the node link is still accessible, the attribute it references will be available
too. However, anonymous attributes cannot be connected to a completely separate geometry
that was created from a different source. To transfer attributes between separate geometries,
the :doc:`/modeling/geometry_nodes/geometry/sample_index` or other similar nodes like the
:doc:`/modeling/geometry_nodes/mesh/sample_nearest_surface` can be used.

.. _attribute-data-types:

Attribute Data Types
====================

The type of an attribute is the kind of data stored at each element.

   :Boolean: True or false value
   :Integer: 32-bit integer
   :8-Bit Integer: Smaller integer with a range from -128 to 127
   :Float: Floating-point value
   :Vector: 3D vector with floating-point values
   :2D Vector: 2D vector with floating-point values
   :Color: RGBA color with 32-bit floating-point values
   :Byte Color: RGBA color with 8-bit positive integer values

The above list is in the order of least to most "complex" (An integer can contain more data than a
boolean, so it is more complicated). When joining separate geometries together, the more complex data
type is preferred when there are matching names. This is particularly important when joining geometry
with named attributes with the :doc:`/modeling/geometry_nodes/geometry/join_geometry`

.. _attribute-domains:

Attribute Domains
=================

The domain of an attribute refers to what type of geometry element the attribute corresponds to.
Knowing the domain of an attribute is important because it defines how it may be interpolated and
used in nodes and shading. You can use the :doc:`Spreadsheet Editor </editors/spreadsheet>`
to determine the domains of attributes.

- **Point** domain attributes are associated with single locations in space with a position:

   - Vertices of a mesh
   - Points of a point cloud
   - Curve control points
- **Edge** domain attributes are associated with the edges of a mesh.
- **Face** domain attributes are associated with the faces of a mesh.
- **Face Corner** domain attributes are associated with the corners of the faces of the mesh.
  An example is a UV map attribute.
- **Spline** domain attributes are associated with a group of connected
  curve control points.
- **Instance** domain attributes exist on the :doc:`/modeling/geometry_nodes/instances` in a geometry.
  They can be used to store different values on copies of geometry data. Instance domain attributes are
  only supported in geometry nodes.

Attributes are automatically interpolated to other domains. For example, when the
:doc:`/modeling/geometry_nodes/input/position` is connected to the selection input of
the :doc:`/modeling/geometry_nodes/material/set_material` node, the values are interpolated
from the *Point* domain to the *Face* domain. Normally, domain conversions use simple averages
for values, but *Boolean* data type attributes have special rules for interpolation:


Boolean Domain Interpolation
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 10 50

   * - From
     - To
     - Conversion

   * - Point
     - Edge
     - An edge is selected if both of its vertices were selected.

   * - Point
     - Face
     - A face is selected if all of its vertices were selected too.

   * - Point
     - Corner
     - Each corner's value is simply a copy of the value at its vertex.

   * - Point
     - Spline
     - A spline is selected if all of its control points were selected.

   * - ..
     - ..
     - ..

   * - Edge
     - Point
     - A vertex is selected if any connected edge was selected.

   * - Edge
     - Face
     - A face is selected if all of its edges are selected

   * - Edge
     - Corner
     - A corner is selected if its two adjacent edges were selected.

   * - ..
     - ..
     - ..

   * - Face
     - Point
     - A vertex is selected if any of the connected faces were selected.

   * - Face
     - Edge
     - An edge is selected if any connected face was selected.

   * - Face
     - Corner
     - Each corner's value is simply a copy of the value at its face.

   * - ..
     - ..
     - ..

   * - Corner
     - Point
     - A vertex is selected if all connected face corners were selected and it is not a loose vertex.

   * - Corner
     - Edge
     - An edge is selected if all corners on adjacent faces were selected.

   * - Corner
     - Face
     - A face is selected if all of its corners were selected.

   * - ..
     - ..
     - ..

   * - Spline
     - Point
     - Each point's value is simply a copy of the corresponding value of the spline.


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
     - Built-in attribute describing vertex or point locations, in the local space of a geometry.
       Any node that changes the location of points will adjust this attribute,
       like the :doc:`/modeling/geometry_nodes/geometry/transform_geometry`
       and the :doc:`/modeling/geometry_nodes/geometry/set_position`.

   * - ``radius``
     - *Float*
     - *Point*
     - A built-in attribute on point clouds used to set the size for the points in the viewport.
       Also built-in on curves, where it controls the size of each curve control point when
       converted to a mesh, or for other operations.

   * - ``id``
     - *Integer*
     - *Point*
     - Created by the :doc:`/modeling/geometry_nodes/point/distribute_points_on_faces`
       to provide stability when the shape of the input mesh changes,
       and used on instances to create motion blur.
       Values are expected to be large, with no order. This attribute is used by nodes
       that generate randomness, like the :doc:`/modeling/geometry_nodes/utilities/random_value`.
       Unlike other built-in attributes, this attribute is not required, and can be removed.

   * - ``material_index``
     - *Integer*
     - *Face*
     - Used to specify the material slot for every face in a mesh.

   * - ``crease``
     - *Float*
     - *Edge*
     - Edge attribute used by the Subdivision Surface modifier.
       The values are limited to a range of 0 and 1.

   * - ``shade_smooth``
     - *Boolean*
     - *Face*
     - Attribute determining if a face should have smooth shading enabled in the viewport or a render.

   * - ``resolution``
     - *Integer*
     - *Spline*
     - Determines the number of evaluated points between two control points of a spline.
       Only NURBS and Bézier splines have this attribute, for poly splines, the value is always one.

   * - ``cyclic``
     - *Boolean*
     - *Spline*
     - Determines whether the spline has a segment that connects its first and last control points.

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
The data type of these attributes can be changed, just like any attribute besides the built-in attributes.
However, the attributes might be expected by Blender to have a certain type.

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

Vertex groups, UV maps and Color Attributes are available as attributes in geometry nodes.
They are referred to by their name.
Naming collisions (e.g. a vertex group and a UV map with the same name) should be avoided.
If there is a naming collision, only one of the attributes is accessible in geometry nodes.

Attributes with any other name can also be created by nodes, when the name is used for the first time.

Note that geometry nodes does not always produce e.g. vertex groups if a node like
:doc:`Join Geometry </modeling/geometry_nodes/geometry/join_geometry>` is used.
Similarly, if the data type of a vertex group attribute is changed from the initial "Float" type,
the attribute will no longer be a vertex group.


.. _bpy.ops.object.attribute_convert:

Attribute Conversion Operator
=============================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_convert.png
   :align: center

This operator found in the *Attributes* panel of the property editor can change the
domain or data type of an attribute.

Due to ongoing development in the area of attributes, many areas of Blender can not yet work with
the generic (identified with a name, stored on any domain with any data type)attributes used by
geometry nodes. That makes this operator an essential workaround in some cases where existing
tools must be used with data generated from geometry nodes.

Mode
   :Generic:
      Interpolate and convert the attribute between the domains and data types described on this page.
   :UV Map:
      Create a :term:`UV Map` layer, editable in the UV editor. These would otherwise
      be represented by a 2D vector attribute on the face corner domain.
   :Vertex Group:
      Create a :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>`
      from the attribute, which corresponds to a float attribute on the point domain.

.. note::

   This operator only works on *original* object data, not including the results of modifiers,
   so any attributes added or changed by geometry nodes will not be affected. To change the type
   of an attribute generated procedurally, modifiers must be applied.
