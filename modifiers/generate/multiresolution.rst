

..    TODO/Review: {{review|im=needs examples}} .


Multiresolution Modifier
========================


.. admonition:: Reference
   :class: refbox

   | Mode:     Object mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg


.. figure:: /images/Multires_modifier_image.jpg
   :width: 500px
   :figwidth: 500px

   Multires modifier


The :guilabel:`Multiresolution` modifier gives the ability to subdivide a mesh to different
levels depending on whether you are viewing it from the 3D Viewport,
Sculpt Mode or a Blender Render.


Options
-------

:guilabel:`Catmull-Clark` / :guilabel:`Simple`
   Set the type of subdivision. :guilabel:`Simple` maintains the current shape, and simply subdivides edges. :guilabel:`Catmull-Clark` creates a smooth surface, smaller than the original.
:guilabel:`Preview`
   Set the level of subdivisions to use in the viewport.
:guilabel:`Sculpt`
   Set the number of subdivisions to use in :guilabel:`Sculpt Mode`\ .
:guilabel:`Render`
   Set the number of subdivisions to use when rendering.

:guilabel:`Subdivide`
   Add a higher level of subdivision.
:guilabel:`Delete Higher`
   Deletes all subdivision levels that are higher than the current one.
:guilabel:`Reshape`
   Copies vertex coordinates from another mesh. To use, select a different mesh with matching topology and vertex coordinates, then :kbd:`Shift` select the mesh and click :guilabel:`Reshape`\ . The mesh will take the shape of the other one.
:guilabel:`Apply Base`
   Modifies the mesh to match the form of the subdivided mesh.

:guilabel:`Optimal Display`
   Skips the drawing of edges added from subdivision.

:guilabel:`Save External`
   Saves displacements to an external .btx file.


