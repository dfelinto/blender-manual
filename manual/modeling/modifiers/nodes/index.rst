.. index:: Modifiers; Geometry Nodes

*****
Nodes
*****

Nodes can be used to modify the objects' geometries in more complex ways.
To use that add a new :doc:`Empty Modifier </modeling/modifiers/generate/empty>`.

This will create a :doc:`Node Group </interface/controls/nodes/groups>` with the
geometry input and output. Those are respectively what is received and passed to the previous and
next modifier in the stack.

.. figure:: /images/modeling_modifiers_nodes_properties.png

   Node group properties exposed in the modifier stack.

Any extra group input is exposed in the modifier itself, and can have unique values even if the
node group is shared among multiple modifiers.


Attribute
=========

.. toctree::
   :maxdepth: 1

   attribute/random_attribute.rst


Color
=========

.. toctree::
   :maxdepth: 1

   color/color_ramp.rst
..
   color/combine_rgb.rst
   color/separate_rgb.rstx


Geometry
========

Nodes that can act on different geometry types (volume, point cloud, mesh).

.. toctree::
   :maxdepth: 1

   geometry/boolean.rst

..
    geometry/transform.rst


Input
======

Nodes used mainly as input to other nodes.

.. toctree::
   :maxdepth: 1

   input/object_info.rst
   input/value.rst
   input/random_float.rst


..
    Mesh
    ====

    Nodes that only act on the mesh geometry.

    .. toctree::
    :maxdepth: 1

    mesh/subdivision_surface.rst
    mesh/edge_split.rst
    mesh/triangulate

..
    Point
    =====

    .. toctree::
    :maxdepth: 1

    point/point_distribute.rst
    point/point_instance.rst


..
    Utilities
    =========

    .. toctree::
    :maxdepth: 1

    utilities/boolean_math.rst
    utilities/clamp.rst
    utilities/float_compare.rst
    utilities/map_range.rst
    utilities/math.rst


..
    Vector
    ======

    .. toctree::
    :maxdepth: 1

    vector/combine_xyz.rst
    vector/separate_xyz.rst
    vector/vector_math.rst
