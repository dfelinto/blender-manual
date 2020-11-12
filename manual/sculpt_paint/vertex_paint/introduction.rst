
************
Introduction
************

Vertex Painting is a simple way of painting color onto an object, by directly
manipulating the color of vertices, rather than textures, and is fairly straightforward.

.. figure:: /images/sculpt-paint_vertex-paint_introduction_mode-menu.png

   Vertex Painting Mode.

When a vertex is painted, the color of the vertex is modified according to
the settings of the brush. The color of all visible planes and edges attached to
the vertex are then modified with a gradient to the color of the other connected vertices.
Note that the color of occluded faces is not modified.

You can also the use :doc:`/render/shader_nodes/input/attribute` to access
vertex color information in the material node tree.
