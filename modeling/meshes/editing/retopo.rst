
..    TODO/Review: {{review|partial=X}} .


Retopologizing
==============

.. admonition:: Note
   :class: note

   In Blender 2.5, the Retopo tool has been replaced by improved mesh snapping functionality. This page will change as retopology tools are updated in newer versions of Blender


Retopology is a common part of modeling workflows. Often times,
a model is created with emphasis on form and detail, however, its topology,
or edge flow is not ideal, or the mesh is very dense, and not efficient.
Modelers can create a new lower resolution mesh that matches the form of the original mesh.


Mesh Snapping
-------------

By enabling snapping, and setting the snap element to Face,
mesh vertices will be projected onto the closest surface in the viewport,
in the view's Z-axis.

This allows you to model freely, without concern for form, and to focus on topology

See :doc:`Snapping <3d_interaction/transform_control/snap_to_mesh>`


Shrinkwrap Modifier
-------------------

The :doc:`Shrinkwrap Modifier <modifiers/deform/shrinkwrap>` is useful in conjunction with face snapping. If edits to the new mesh have been made with snapping disabled, the shrinkwrap modifier will allow you to stick the new mesh to the old mesh, as if you were shrinkwrapping it.


