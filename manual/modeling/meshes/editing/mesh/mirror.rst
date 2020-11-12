
******
Mirror
******

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Mirror`
   :Hotkey:    :kbd:`Ctrl-M`

The Mirror tool mirrors a selection across a selected axis.

The Mirror tool in *Edit Mode* is similar to
:doc:`Mirroring in Object Mode </scene_layout/object/editing/mirror>`.
It is exactly equivalent to scaling vertices by -1 around one chosen pivot point
and in the direction of one chosen axis, only it is faster/handier.

After this tool becomes active, select an axis to mirror the selection
by pressing :kbd:`X`, :kbd:`Y`, or :kbd:`Z`.

You can also interactively mirror the geometry by holding the :kbd:`MMB` and dragging in
the desired mirror direction.


Axis of Symmetry
================

For each transformation orientation,
you can choose one of its axes along which the mirroring will occur.

As you can see, the possibilities are infinite and the freedom complete:
You can position the pivot point at any location around which we want the mirroring to occur,
choose one transformation orientation and then one axis on it.


Pivot Point
===========

:doc:`Pivot points </editors/3dview/controls/pivot_point/index>` must be set first.
Pivot points will become the center of symmetry.
If the widget is turned on it will always show where the pivot point is.

In Fig. :ref:`fig-mesh-deform-mirror-origins` the pivot point default to
median point of the selection of vertices in *Edit Mode*.
This is a special case of the *Edit Mode* as explained on
the :doc:`pivot point page </editors/3dview/controls/pivot_point/index>`.

.. _fig-mesh-deform-mirror-origins:

.. list-table:: Mirror around the individual origins.

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirror.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_individual-after.png
          :width: 320px

          Mesh after mirrored along X axis.

In Fig. :ref:`fig-mesh-deform-mirror-cursor` the pivot point is the *3D Cursor*,
the transformation orientation is *Local*, a.k.a. the object space,
and the axis of transformation is X.

.. _fig-mesh-deform-mirror-cursor:

.. list-table:: Mirror around the 3D Cursor.

   * - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-before.png
          :width: 320px

          Mesh before mirror.

     - .. figure:: /images/modeling_meshes_editing_mesh_mirror_cursor-after.png
          :width: 320px

          Mesh after mirrored along X axis using the 3D cursor as a pivot point.


Transformation Orientations
===========================

:doc:`Transformation Orientations </editors/3dview/controls/orientation>`
are found on the 3D Viewport header, next to the *Widget* buttons.
They decide which coordinate system will rule the mirroring.
