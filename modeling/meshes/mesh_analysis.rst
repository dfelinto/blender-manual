..    TODO/Review: {{review|split=X|text=splitted mesh - mesh analysis}} .


Mesh Analysis
-------------

Mesh analysis is useful for displaying attributes of the mesh that may impact certain use
cases.

The mesh analysis works in editmode and shows areas with a high value in red,
and areas with a low value in blue.
Geometry outside the range is displayed grey.

Currently the different modes target 3d-printing as their primary use.


Overhang
~~~~~~~~

.. figure:: /images/editmode_mesh_statvis_overhang.jpg
   :height: 260px

   Overhang


Extrusion 3D printers have a physical limit to the overhang that can be printed,
this display mode shows the overhang with angle range and axis selection.


Thickness
~~~~~~~~~

.. figure:: /images/editmode_mesh_statvis_thick.jpg
   :height: 260px

   Thickness


Printers have a limited *wall-thickness* where very thin areas can't be printed,
this test uses ray casting and a distance range to the thickness of the geometry.


Intersections
~~~~~~~~~~~~~

.. figure:: /images/editmode_mesh_statvis_intersect.jpg
   :height: 260px

   Intersecting faces


Another common cause of problems for printing are intersections between surfaces,
where the inside/outside of a model can't be reliably detected.

Unlike other display modes, intersections have no variance and are either on or off.


Distortion
~~~~~~~~~~

.. figure:: /images/editmode_mesh_statvis_distort.jpg
   :height: 260px

   Distorted Faces


Distorted geometry can cause problems since the triangulation of a distorted ngon is undefined.

Distortion is measured by faces which are not flat,
with parts of the face pointing in different directions.


Sharp Edges
~~~~~~~~~~~

.. figure:: /images/editmode_mesh_statvis_sharp.jpg
   :height: 260px

   Sharp edges


Similar to wall-thickness, sharp edges can form shapes that are too thin to be able to print.


.. admonition:: Warning
   :class: note


    .. warning::

      FIXME - warning body below

   There are some known limitations with mesh analysis


   - Currently only displayed with deform modifiers.
   - For high-poly meshes is slow to use while editing the mesh.


