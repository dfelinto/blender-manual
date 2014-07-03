
Median Point as Pivot
=====================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     Select from the following icon in the 3D window header

   .. figure:: /images/Icon-library_3D-Window_header-pivot-point.jpg
   | Hotkey:   :kbd:`ctrl-,`


The :guilabel:`Median Point` can be considered to be broadly similar to the concept of Center
of Gravity (COG). If we assume that every element (Object, face, vertex etc)
of the selection has the same mass,
the median point would sit at the point of equilibrium for the selection (the COG).


In Object Mode
--------------

In Object Mode, Blender only considers the Object centers when determining the median point.
This can lead to some counterintuitive results. In the Object Mode median points image below,
you can see that the median point is between the Object centers and can be nowhere near the
Objects' mesh.


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Median_point-median-point-objects.jpg
   :width: 640px
   :figwidth: 640px

   Median points in Object Mode. The Median point is indicated by the yellow dot.


In Edit Mode
------------

In Edit Mode,
the median point is determined via the part of the selection that has the most elements.
For example, in the *Median points in Edit Mode* image,
when there are two cubes with an equal number of vertices,
the median point lies directly between the two cubes. However,
if we subdivide one cube multiple times so that it has many more vertices,
you can see that the median point has shifted to the region with the most vertices.


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Median_point-median-point-vertices.jpg
   :width: 640px
   :figwidth: 640px

   Median points in Edit Mode. The Median point is indicated by the yellow dot.


