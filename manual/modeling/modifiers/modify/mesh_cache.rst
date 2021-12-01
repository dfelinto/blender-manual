.. index:: Modeling Modifiers; Mesh Cache Modifier
.. _bpy.types.MeshCacheModifier:

*******************
Mesh Cache Modifier
*******************

The Mesh Cache modifier main use is for animated mesh data to be applied to a mesh and
played back, deforming the mesh.

This works in a similar way to :doc:`shape keys </animation/shape_keys/introduction>`,
but is aimed at playing back external files and is often used for interchange between applications.

.. tip::

   Both MDD and PC2 depend on the vertex order on the mesh remaining unchanged.
   This is a limitation of this method, so take care not to add, remove or reorder vertices
   once this modifier is used.


Options
=======

.. figure:: /images/modeling_modifiers_modify_mesh-cache_panel.png
   :align: right
   :width: 300px

   Mesh Cache Modifier.

Format
   The input file format (currently ``.mdd`` and ``.pc2`` are supported).

File Path
   Path to the cache file.

Influence
   Factor to adjust the influence of the modifier's deformation, useful for blending in/out from the cache data.

Deform Mode
   This setting defaults to *Overwrite* which will replace the vertex locations with those in the cache file.
   However, you may want to use shape keys, for example, and mix them with the mesh cache.
   In this case you can select the *Deform* option which integrates deformations with the mesh cache result.

   .. note::

      This feature is limited to making smaller, isolated edits and
      will not work for larger changes such as re-posing limbs.

Interpolation
   *None*, or *Linear*, which will blend between frames.
   Use linear when the frames in the cache file do not match up exactly with the frames in the blend-file.

Vertex Group
   If set, restrict the effect to the only vertices in that vertex group.

   Invert ``<->``
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.


Time Remapping
--------------

Time Mode
   Select how time is calculated.

   :Frame:
      Allows you to control the frames,
      which will ignore timing data in the file but is often useful since it gives simple control.
   :Time:
      Evaluates time in seconds,
      taking into account timing information from the file (offset and frame-times).
   :Factor:
      Evaluates the entire animation as a value in the [0, 1] range.

Play Mode
   Select how playback operates.

   :Scene:
      Use the current frame from the scene to control playback.

      Frame Start
         Play the cache starting from this frame.
      Frame Scale
         Scale time by this factor (applied after the start value).

   :Custom:
      Control animation timing manually.

      Evaluation Value
         Property used for animation time,
         this gives more control of timing (typically this value will be animated).


Axis Mapping
------------

Forward/Up Axis
   The axis for forward and up used in the source file.

Flip Axis
   In rare cases you may also need to flip the coordinates on an axis.
