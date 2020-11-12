
******************
Adaptive Sculpting
******************

In order for sculpting to give accurate and predictable results, Blender needs geometry to work with.
One way to accomplish this is starting off with a highly subdivided mesh.
The other way involves using either of two adaptive sculpting methods to add geometry dynamically.


Dynamic Topology
================

Dynamic topology (aka dyntopo) is a dynamic tessellation
sculpting method that adds and removes details under the brush.
This works by first tessellating the mesh then applying the sculpting stroke on top of the tessellated mesh.

This makes it possible to sculpt complex shapes out of a simple mesh,
rather than just adding details onto a modeled base mesh.

.. seealso::

   Dynamic Topology can be enabled in the :doc:`Dyntopo panel </sculpt_paint/sculpting/tool_settings/dyntopo>`.


Multiresolution Modifier
========================

The Multiresolution Modifier can be used to dynamically subdivide the mesh.
The more subdivision the more computing will be needed. With the Blender stack
non-destructive data, multiresolution sculpting will help when you have a clean topology base mesh.

When sculpting with multiple resolutions you have the ability to sculpt in different levels of subdivision,
this mean you can sculpt some details in subdivision level 1 and add more details in
subdivision 2 and go back to subdivision 1 correct some mistakes. While this workflow is
often used, the Multiresolution Modifier has some limitations. You may end up with some mesh distortions.
As an advice, add as most details as possible before adding more subdivisions.
Clay brush works better with multiresolution sculpting to sculpt secondary forms.

- Step up one multires level :kbd:`PageUp`
- Step down one multires level :kbd:`PageDown`
- Set multires level :kbd:`Ctrl-0` to :kbd:`Ctrl-5`

.. seealso::

   Read more about the :doc:`Multiresolution Modifier </modeling/modifiers/generate/multiresolution>`.
