.. _bpy.ops.mesh.face_shading:

*******************
Shade Smooth & Flat
*******************

The appearance of the mesh edges are determined to be evened out or well defined within the 3D Viewport and render.
In Edit Mode, individual faces can be selected to determine which faces are smoothed or flattened.

.. note::

   Both :doc:`Shade Smooth and Flat </scene_layout/object/editing/shading>`
   are also available in Object Mode and function the same way.


.. _bpy.ops.mesh.faces_shade_smooth:

Shade Smooth
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Shade Smooth`

Using interpolated vertex normals, the mesh faces will blur at the edges and appear smooth.


.. _bpy.ops.mesh.faces_shade_flat:

Shade Flat
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Shade Flat`

Face normals are displayed evenly, because of this all the edges of the selected mesh will be easily visible.

.. tip::

   Use the :doc:`Edge Split </modeling/modifiers/generate/edge_split>`
   modifier and :doc:`Auto Smooth </modeling/meshes/structure>`
   within the mesh data properties to balance between smooth surfaces and sharp edges.
