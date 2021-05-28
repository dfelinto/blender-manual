
*************
Tool Settings
*************

Options
=======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Tool tab --> Options panel`


Transform
---------

.. _bpy.types.ToolSettings.use_transform_correct_face_attributes:

Correct Face Attributes
   Adjust geometry attributes like :doc:`UVs </modeling/meshes/uv/index>`
   and :doc:`Vertex Colors </sculpt_paint/vertex_paint/index>` while transforming.

.. _bpy.types.ToolSettings.use_transform_correct_keep_connected:

Keep Connected
   Merge attributes connected to the same vertex while using *Correct Face Attributes*.

   .. tip::

      Keeping UVs connected is useful for organic modeling, but not for architectural modeling.


UVs
---

.. _bpy.types.ToolSettings.use_edge_path_live_unwrap:

Live Unwrap
   Automatically recalculates the UV unwrapping every time an edge has its seam property changed.
   Note, this is different than the :ref:`Live Unwrap <bpy.types.SpaceUVEditor.use_live_unwrap>`
   option in the UV Editor.


.. _bpy.types.Mesh.use_mirror_x:
.. _bpy.types.Mesh.use_mirror_y:
.. _bpy.types.Mesh.use_mirror_z:
.. _modeling_meshes_tools-settings_mirror:

Mirror
------

Mirror allows you to transform vertices symmetrically according to the chosen axis.
When you transform an element (vertex, edge or face),
if there is its exact axis-mirrored counterpart (in local space),
it will be transformed accordingly, through a symmetry along the chosen axis.

.. note::

   The conditions for *Mirror* to work are quite strict, which can make it difficult to use.
   To have an exact mirrored version of a (half) mesh,
   it's easier and simpler to use the :doc:`Mirror Modifier </modeling/modifiers/generate/mirror>`.


.. _bpy.types.Mesh.use_mirror_topology:

Topology Mirror
---------------

.. note::

   For *Topology Mirror* to work, at least one of the three *Mirror Axis* must be enabled.

When using any of the three *Mirror Axis* options to work on a mirrored Mesh Geometry, the vertices that
are mirrored must be perfectly placed. If they are not exactly positioned in their mirror
locations then the *Mirror Axis* will not treat those vertices as mirrored.

*Topology Mirror* tries to address this problem by determining which vertices are mirrored vertices not only by
using their positions but also by looking at how those vertices are related to others in the Mesh Geometry.
It looks at the overall topology to determine if particular vertices will be treated as mirrored.
The effect of this is that mirrored vertices can be non-symmetrical and yet still be treated as mirrored.

.. note::

   The *Topology Mirror* functionality will work more reliably on mesh geometry
   which is more detailed. If you use very simple geometry, for example
   a *Cube* or *UV Sphere*, the *Topology Mirror* option will often not work.


Example
^^^^^^^

For an example of how to use *Topology Mirror* open up a new Blender scene,
then delete the default cube and add a Monkey object to the 3D Viewport.

#. Press :kbd:`Tab` to put the Monkey object into *Edit Mode*.
#. With all the *Mirror Axis* options disabled move one of the Monkey object's vertices slightly.
#. Then Turn the *X Axis Mirror* on but leave *Topology Mirror* disabled.
#. If you now move that vertex again, the *X Axis Mirror* will not work and the mirrored
   vertices will not be altered.
#. If you then enable *Topology Mirror* and move the same vertices again,
   then *X Axis Mirror* should still mirror the other vertex,
   even though they are not perfectly positioned.


.. _bpy.types.ToolSettings.use_mesh_automerge:

Auto Merge Vertices
-------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Sidebar --> Tool --> Options --> Auto Merge Vertices`

When enabled, as soon as a vertex moves closer to another one
than the *Threshold* setting, they are automatically merged.
This option affects interactive operations only
(tweaks made in the :ref:`bpy.ops.screen.redo_last` panel are considered interactive too).
If the exact spot where a vertex is moved contains more than one vertex,
then the merge will be performed between the moved vertex and one of those.

.. _bpy.types.ToolSettings.use_mesh_automerge_and_split:

Split Edges & Faces
   Detects the intersection of each transformed edge, creating a new vertex in place
   and sectioning the edge and the face if any.

.. _bpy.types.ToolSettings.double_threshold:

Threshold
   Defines the maximum distance between vertices that are merged.
