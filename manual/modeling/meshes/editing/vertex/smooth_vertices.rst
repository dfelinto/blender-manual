.. _bpy.ops.mesh.vertices_smooth:
.. _tool-mesh-smooth:

***************
Smooth Vertices
***************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Smooth Vertices`,
               :menuselection:`Context Menu --> Smooth`

This tool smooths the selected vertices by averaging the angles between the faces.
After using the tool, options appear in the *Toolbar*:

Smoothing
   Smoothing factor.
Repeat
   The number of smoothing iterations.
Axes
   Limit the effect to certain axes.

.. list-table::

   * - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-before.png
          :width: 200px

          Mesh before smoothing.

     - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-one-iteration.png
          :width: 200px

          Mesh after one smoothing iteration.

     - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-ten-iterations.png
          :width: 200px

          Mesh after ten smoothing iterations.

.. seealso:: Subdividing

   Adjusting the *smooth* option after using
   the :doc:`Subdivide </modeling/meshes/editing/edge/subdivide>` tool
   results in a more organic shape.

.. seealso:: Smooth Modifier

   The :doc:`Smooth Modifier </modeling/modifiers/deform/smooth>`, which can be limited to a *Vertex Group*,
   is a non-destructive alternative to the Smooth tool.
